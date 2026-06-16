# services/rag_service.py
# app/services/rag_service.py
import uuid
import chromadb
from app.services.gemini_service import ask_gemini
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="company_knowledge"
)
def ingest_chunks(chunks, filename):

    ids = []
    metadatas = []

    for i, chunk in enumerate(chunks):

        ids.append(str(uuid.uuid4()))

        metadatas.append({
            "source": filename,
            "chunk_number": i
        })

    collection.add(
        documents=chunks,
        ids=ids,
        metadatas=metadatas
    )

    return len(chunks)

def search_chunks(question):

    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    print("\nDistances:")
    print(results["distances"])
    print(results["metadatas"])
    return results


def build_context(results):

    documents = results["documents"][0]

    context = "\n\n".join(documents)

    return context


def answer_question(question):
    print("NEW VERSION OF answer_question IS RUNNING")

    results = search_chunks(question)

    best_distance = results["distances"][0][0]

    print("Best Distance:", best_distance)

    DISTANCE_THRESHOLD = 1.5

    if best_distance > DISTANCE_THRESHOLD:
        return "This question does not appear to be related to our company."

    context = build_context(results)

    prompt = f"""
Answer ONLY from the provided company knowledge.

Context:
{context}

Question:
{question}

If the answer is not contained in the context,
say:
I could not find this information in the company knowledge base.
"""

    return ask_gemini(prompt)

