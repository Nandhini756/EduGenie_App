from ..gemini_client import get_gemini


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""Create a structured and adaptive learning path for a student who wants to learn about: {topic}

Include, when appropriate:
- Beginner level: foundations and estimated time.
- Intermediate level: concepts that build on the foundations and estimated time.
- Advanced level: deeper concepts and estimated time.
- Key topics in a sensible order.
- A few reputable learning-resource types or examples.
- Practical study tips.
Keep it useful and realistic. Do not claim a resource has been verified if you cannot verify it.
"""
    return get_gemini().generate(
        prompt,
        system_instruction="You are EduGenie, an adaptive learning-path planner.",
        temperature=0.5,
        max_output_tokens=1800,
    )
