# retrieval/prompt_builder.py

def build_prompt(user_query, retrieved_chunks):
    system_instruction = (
        "You are a helpful travel planner AI. Use the following travel data to answer the user's query. "
        "Be specific, budget-conscious, and creative."
    )
    context = "\n\n".join(retrieved_chunks)
    prompt = f"""{system_instruction}

Context:
{context}

User Query:
{user_query}

Answer:"""
    return prompt
