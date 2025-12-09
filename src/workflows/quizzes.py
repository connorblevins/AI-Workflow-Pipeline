from src.llm.gpt_client import generate_text

def generate_quiz(raw_text: str) -> str:
    """
    Generate practice questions (and brief answers) from the source material.
    """
    prompt = f"""
You are an AI tutor creating practice questions for a college student.

Input material:
\"\"\"{raw_text}\"\"\"

Goals:
1. Identify the key skills, procedures, and reasoning patterns in the material.
2. Create a mix of question types:
   - Conceptual (explain/compare/why)
   - Applied (work through an example, scenario, or small problem)
   - Checkpoints (quick short-answer checks)
3. Make questions challenging but appropriate for a first pass of studying.
4. Provide concise model answers or solution outlines after each question.
5. When creating these cards make sure to add a space such as question on line 1 and answer on line 2
Return the result in markdown using this format:


1. **Question:** ...
   **Answer (short):** ...

2. **Question:** ...
   **Answer (short):** ...

Aim for 8–20 questions depending on the material length.
"""
    return generate_text(prompt)