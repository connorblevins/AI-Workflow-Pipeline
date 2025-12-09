from src.llm.gpt_client import generate_text


def find_prerequisites(raw_text: str) -> str:
    """
    Generate a prerequisite concept map from the source material.
    """
    prompt = f"""
You are an AI curriculum designer. Analyze the material and build a prerequisite map of concepts.

Input material:
\"\"\"{raw_text}\"\"\"

Goals:
1. Identify the main target concepts or skills in the material.
2. For each target concept, list what a student should already understand first.
3. Organize concepts from most basic → intermediate → advanced.
4. Keep it compact and readable, so a student can see what to review before moving on.
5. Use only information that can be reasonably inferred from the text.

Return the result in markdown in this structure:

### Concept Levels

- **Level 1 (Foundations):**
  - Concept A
  - Concept B
- **Level 2 (Builds on Level 1):**
  - Concept C (requires: A, B)
  - Concept D (requires: B)
- **Level 3 (Advanced):**
  - Concept E (requires: C, D)

### Prerequisite Pairs

- A → C
- B → C
- B → D
- C, D → E

Use the concepts that appear in the input material, and fill out both sections.
"""
    return generate_text(prompt)