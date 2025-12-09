from src.llm.gpt_client import generate_text

def generate_study_plan(raw_text: str) -> str:
    prompt = f"""
You are an AI study planner for college students.

Input material:
\"\"\"{raw_text}\"\"\"

1. Identify key topics.
2. Build a 3–7 day study plan with sessions of 30–90 minutes.
3. Emphasize active recall and spaced repetition.
4. Keep it concise and numbered.

Return the plan in markdown format.
"""
    return generate_text(prompt)