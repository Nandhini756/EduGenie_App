# EduGenie — AI Tutor

EduGenie is a FastAPI web application implementing the five AI-tutor functions described in the supplied project documentation:

1. Q&A — `GET /qa`
2. Topic explanation — `POST /explain/`
3. Paragraph summarization — `POST /summarize/`
4. Three-question quiz generation — `POST /quiz`
5. Adaptive learning recommendations — `GET /learn/recommendations`

The supplied documentation is included at `docs/project_documentation.docx` for reference.

## VS Code / Windows setup

Open the `edugenie` folder in VS Code, then open Terminal → New Terminal.

```cmd
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Create `.env` from `.env.example` and put your Gemini API key in `GEMINI_API_KEY`.

Then run:

```cmd
python -m uvicorn app.main:app --reload
```

Open:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/health

## Tests

With the virtual environment active:

```cmd
pytest
```

The included tests do not consume Gemini quota; they test the homepage and health endpoint.

## Gemini quota errors

If Gemini returns `429 RESOURCE_EXHAUSTED`, the project has reached the quota available to the configured API project/model. Changing Python code will not restore that quota. Use a project/key with available quota or wait for the applicable quota reset.

If Gemini returns `503 UNAVAILABLE` because the model is temporarily busy, retry later or select another model available to your project by changing `GEMINI_MODEL` in `.env`.

Never commit or share `.env` or your API key.
