import json
from typing import Any

from ..gemini_client import get_gemini


def _validate_quiz(data: Any) -> list[dict[str, Any]]:
    if not isinstance(data, list) or len(data) != 3:
        raise ValueError("Quiz response must contain exactly 3 questions.")

    result: list[dict[str, Any]] = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Each quiz question must be an object.")
        question = item.get("question")
        options = item.get("options")
        answer = item.get("answer")
        if not isinstance(question, str) or not question.strip():
            raise ValueError("Each question needs text.")
        if not isinstance(options, list) or len(options) != 4 or not all(isinstance(x, str) for x in options):
            raise ValueError("Each question needs exactly 4 text options.")
        if not isinstance(answer, str) or answer not in options:
            raise ValueError("The answer must exactly match one option.")
        result.append({"question": question.strip(), "options": [x.strip() for x in options], "answer": answer.strip()})
    return result


def generate_quiz(text: str) -> list[dict[str, Any]]:
    prompt = f"""Create exactly 3 multiple-choice questions about the topic or passage below.
Each object must contain:
- question: string
- options: exactly 4 strings
- answer: exactly one of the option strings

Make questions educational and unambiguous. Return JSON only.

Topic/passage:
{text}
"""
    raw = get_gemini().generate(
        prompt,
        system_instruction="You generate clean, valid JSON for an educational quiz.",
        temperature=0.4,
        max_output_tokens=1400,
        response_mime_type="application/json",
    )
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError("Gemini returned invalid quiz JSON.") from exc
    return _validate_quiz(data)
