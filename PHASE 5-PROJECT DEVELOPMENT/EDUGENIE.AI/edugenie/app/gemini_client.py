from functools import lru_cache

from .config import get_settings


class GeminiService:
    def __init__(self) -> None:
        from google import genai

        settings = get_settings()
        if not settings.gemini_api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is not configured. Add it to the .env file before using AI features."
            )
        self.client = genai.Client(api_key=settings.gemini_api_key)
        self.model = settings.gemini_model

    def generate(
        self,
        prompt: str,
        *,
        system_instruction: str | None = None,
        temperature: float = 0.4,
        max_output_tokens: int = 1200,
        response_mime_type: str | None = None,
    ) -> str:
        from google.genai import types

        config = types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_output_tokens,
            system_instruction=system_instruction,
            response_mime_type=response_mime_type,
        )
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=config,
        )
        text = getattr(response, "text", None)
        if not text:
            raise RuntimeError("Gemini returned an empty response.")
        return text.strip()


@lru_cache
def get_gemini() -> GeminiService:
    return GeminiService()
