from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from starlette.middleware.cors import CORSMiddleware

from .config import get_settings
from .modules.explanation import explain_topic
from .modules.learning_path import get_learning_recommendations
from .modules.qna import answer_question_with_gemini
from .modules.quiz import generate_quiz
from .modules.summary import summarize_text

BASE_DIR = Path(__file__).resolve().parent
settings = get_settings()

app = FastAPI(title=settings.app_name, version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


class TopicRequest(BaseModel):
    topic: str = Field(min_length=1, max_length=500)


class TextRequest(BaseModel):
    text: str = Field(min_length=1, max_length=20000)


@app.get("/", include_in_schema=False)
async def home() -> FileResponse:
    return FileResponse(BASE_DIR / "templates" / "index.html")


@app.get("/health")
async def health() -> dict[str, str | bool]:
    return {
        "status": "ok",
        "ai_configured": bool(settings.gemini_api_key),
        "model": settings.gemini_model,
    }


@app.get("/qa")
async def answer_question(question: str = Query(..., min_length=1, max_length=4000)) -> dict[str, str]:
    try:
        return {"answer": answer_question_with_gemini(question.strip())}
    except Exception as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc


@app.post("/explain/")
async def explain_api(payload: TopicRequest) -> dict[str, str]:
    try:
        topic = payload.topic.strip()
        return {"topic": topic, "explanation": explain_topic(topic)}
    except Exception as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc


@app.post("/summarize/")
async def summarize_api(payload: TextRequest) -> dict[str, str]:
    try:
        return {"summary": summarize_text(payload.text.strip())}
    except Exception as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc


@app.post("/quiz")
async def quiz_api(payload: TextRequest) -> dict[str, list[dict]]:
    try:
        return {"quiz": generate_quiz(payload.text.strip())}
    except ValueError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc


@app.get("/learn/recommendations")
async def learning_recommendation_api(
    topic: str = Query(..., min_length=1, max_length=500),
) -> dict[str, str]:
    try:
        clean_topic = topic.strip()
        return {
            "topic": clean_topic,
            "recommendation": get_learning_recommendations(clean_topic),
        }
    except Exception as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
