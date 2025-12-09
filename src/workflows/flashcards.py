from src.llm.gpt_client import generate_text

def generate_flashcards(raw_text: str) -> str:
    """
    Generate Q/A flashcards from the source material.
    """
    prompt = f"""
You are an AI assistant that creates high-yield flashcards for college students.

Input material:
\"\"\"{raw_text}\"\"\"

Goals:
1. Extract the most important concepts, definitions, formulas, and facts.
2. Write clear, single-focus Q/A flashcards that encourage active recall.
3. Prefer "why/how" questions when possible, not only pure definitions.
4. Keep each answer short (1–4 sentences or a short list).
5. Avoid duplicates and overly trivial cards.

Return the flashcards in markdown in this format:


1. **Q:** ...
   **A:** ...

2. **Q:** ...
   **A:** ...

Include 10–30 flashcards depending on how dense the material is.
"""
    return generate_text(prompt)