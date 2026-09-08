from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.models import FormData
from app.llm import analyze_lead
from app.sheets import add_lead


app = FastAPI(
    title="AI Form To Google Sheets",
    description="AI powered lead collection system",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {
        "message": "AI Form To Google Sheets API is running"
    }


@app.post("/submit")
def submit_form(form_data: FormData):

    try:
        print("1. Form received")

        # Groq LLM
        ai_result = analyze_lead(form_data)

        print("2. Groq response:")
        print(ai_result)

        # Google Sheets
        add_lead(form_data, ai_result)

        print("3. Data added to Google Sheet")

        return {
            "success": True,
            "message": "Form submitted successfully",
            "ai_analysis": ai_result
        }

    except Exception as e:

        print("❌ ERROR:", repr(e))

        return {
            "success": False,
            "message": str(e)
        }


app.mount(
    "/frontend",
    StaticFiles(directory="frontend"),
    name="frontend"
)