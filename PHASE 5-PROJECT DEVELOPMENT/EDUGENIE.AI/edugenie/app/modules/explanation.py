from ..gemini_client import get_gemini


def explain_topic(topic: str) -> str:
    prompt = f"""Explain the concept of '{topic}' in a simple, clear way for a school student.
Structure the answer with:
1. A one-sentence definition.
2. A simple explanation.
3. One everyday or easy academic example.
4. One short takeaway.
Avoid unnecessary jargon.
"""
    return get_gemini().generate(
        prompt,
        system_instruction="You are EduGenie, a patient school-level tutor.",
        temperature=0.5,
        max_output_tokens=900,
    )
