# # retrieval/llm_caller.py

# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def call_llm(prompt, model="gpt-3.5-turbo", temperature=0.7):
#     try:
#         response = openai.ChatCompletion.create(
#             model=model,
#             messages=[
#                 {"role": "system", "content": "You are a helpful travel planner."},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=temperature,
#             max_tokens=1000
#         )
#         return response["choices"][0]["message"]["content"]
#     except Exception as e:
#         return f"Error calling LLM: {e}"

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def call_llm(prompt, model="gpt-3.5-turbo", temperature=0.7):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful travel planner."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling LLM: {e}"
