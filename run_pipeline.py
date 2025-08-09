# run_pipeline.py

from retrieval.retriever import retrieve_top_chunks
from retrieval.prompt_builder import build_prompt
from retrieval.llm_caller import call_llm

# def run_travel_planner(query):
#     print(f"🔍 User Query: {query}\n")

#     # Step 1: Retrieve relevant chunks
#     chunks = retrieve_top_chunks(query)
#     print("📚 Retrieved Chunks:")
#     for i, chunk in enumerate(chunks, 1):
#         print(f"[{i}] {chunk}")

#     # Step 2: Build prompt
#     prompt = build_prompt(query, chunks)

#     # Step 3: Call LLM
#     response = call_llm(prompt)
#     print("\n🧳 Generated Travel Plan:\n")
#     print(response)

def run_travel_planner(query):
    print(f"🔍 User Query: {query}\n")

    # Step 1: Retrieve relevant chunks
    chunks = retrieve_top_chunks(query)
    print("Retrieved Chunks:")
    for i, chunk in enumerate(chunks, 1):
        print(f"[{i}] {chunk}")

    # Limit chunks to avoid context overflow
    max_chunks = 5
    chunks = chunks[:max_chunks]

    # Step 2: Build prompt
    prompt = build_prompt(query, chunks)

    # Step 3: Call LLM
    response = call_llm(prompt)
    print("\n🧳 Generated Travel Plan:\n")
    print(response)

if __name__ == "__main__":
    user_query = "Plan a 3-day trip to Tokyo under $1000"
    run_travel_planner(user_query)
