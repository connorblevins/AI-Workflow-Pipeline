import streamlit as st
from openai import OpenAI

GPT_API_KEY = st.secrets.get("GPT_API_KEY")

if GPT_API_KEY is None:
    raise RuntimeError("GPT_API_KEY not set in Streamlit secrets.")

client = OpenAI(api_key=GPT_API_KEY)

def generate_text(prompt: str, model: str = "gpt-5-nano") -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
