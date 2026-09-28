from ..gemini_client import get_gemini


def summarize_text(text: str) -> str:
    prompt = f"""Summarize the following text in simple language.
Keep the important facts and main idea. Use a short paragraph or concise bullet points.
Do not add facts that are not present in the source text.

Text:
{text}
"""
    return get_gemini().generate(
        prompt,
        system_instruction="You are EduGenie, a concise summarization tutor.",
        temperature=0.2,
        max_output_tokens=900,
    )
