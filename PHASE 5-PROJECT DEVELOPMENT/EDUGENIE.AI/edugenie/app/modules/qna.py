from ..gemini_client import get_gemini


def answer_question_with_gemini(question: str) -> str:
    prompt = f"""Answer the student's question accurately and clearly.
Use simple language suitable for a school student. If the question is ambiguous, briefly state the assumption you made.

Student question:
{question}
"""
    return get_gemini().generate(
        prompt,
        system_instruction="You are EduGenie, a helpful and age-appropriate AI tutor.",
        temperature=0.3,
        max_output_tokens=700,
    )
