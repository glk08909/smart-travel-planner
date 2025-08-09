# retrieval/prompt_builder.py

def build_prompt(user_query, retrieved_chunks):
    """
    Constructs a prompt for the LLM using retrieved context and the user's query.
    """
    system_instruction = (
        "You are a helpful travel planner AI. Use the following travel data to answer the user's query. "
        "Be specific, budget-conscious, and creative."
    )
    
    # Combine retrieved chunks into a single context block
    context = "\n\n".join(retrieved_chunks)
    
    # Format the full prompt
    prompt = f"""{system_instruction}

Context:
{context}

User Query:
{user_query}

Answer:"""
    
    return prompt

# Optional: test the function directly
if __name__ == "__main__":
    user_query = "Plan a 3-day trip to Tokyo under $1000"
    retrieved_chunks = [
        "Tokyo hotels under $100/night include Hotel Gracery and APA Hotel.",
        "The Tokyo Metro pass costs around $15 for 3 days.",
        "Top free attractions: Meiji Shrine, Ueno Park, and Senso-ji Temple.",
        "Street food in Asakusa and Tsukiji offers meals under $10.",
        "Day trips to Yokohama cost around $5 by train."
    ]

    prompt = build_prompt(user_query, retrieved_chunks)
    print(prompt)
