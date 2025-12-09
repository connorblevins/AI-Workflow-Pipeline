import streamlit as st
from pathlib import Path

from src.utils.parsing import extract_text_from_file
from src.workflows.study_plan import generate_study_plan
from src.workflows.quizzes import generate_quiz

st.set_page_config(
    page_title="AI Study Workflow Companion",
    layout="wide",
)

st.title("AI Study Workflow Companion")
st.write("Paste your lecture slides, chapters, assignments, code, or notes, and I'll help you study smarter. Text input holds priority over uploaded files.")
st.write("We will provide you with a study plan, flashcards, practice questions, and the prerequisites for whatever class you are trying to learn!")

input_text = st.text_area(
    "Paste your material here:",
    height=250,
    placeholder="Lecture slides, textbook chapters, assignment instructions, or notes...",
)

uploaded_files = st.file_uploader(
    "Upload your study materials (slides, chapters, assignments, notes, etc.)",
    type=["pdf", "pptx", "docx", "txt"],
    accept_multiple_files=True,
)

if not uploaded_files:
    st.info("Upload one or more files to get started.")
else:
    st.success(f"Received {len(uploaded_files)} file(s).")

generateAidsButton = st.button("Generate Study Aids", type="primary")

if  generateAidsButton and input_text.strip():
    with st.spinner("Thinking about your material..."):
            
            plan = generate_study_plan(input_text)
            st.subheader("Personalized Study Plan")
            st.markdown(plan)


            
            flashcards = generate_flashcards(input_text)
            st.subheader("Flashcards")
            st.markdown(flashcards)

            
            quiz = generate_quiz(input_text)
            st.subheader("Practice Questions")
            st.markdown(quiz)

            
            prereq_map = find_prerequisites(input_text)
            st.subheader("Prerequisite Concepts")
            st.markdown(prereq_map)
elif generateAidsButton and uploaded_files:

    all_text = ""
    for f in uploaded_files:
        file_text = extract_text_from_file(f)
        all_text += f"\n\n===== {f.name} =====\n\n" + file_text

    with st.spinner("Thinking about your material..."):
            
            plan = generate_study_plan(all_text)
            st.subheader("Personalized Study Plan")
            st.markdown(plan)


            
            flashcards = generate_flashcards(all_text)
            st.subheader("Flashcards")
            st.markdown(flashcards)

            
            quiz = generate_quiz(all_text)
            st.subheader("Practice Questions")
            st.markdown(quiz)

            
            prereq_map = find_prerequisites(all_text)
            st.subheader("Prerequisite Concepts")
            st.markdown(prereq_map)
else:
    st.info("Paste your content above and click **Generate Study Aids** to get started.")
