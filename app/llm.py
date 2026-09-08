import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_lead(form_data):

    prompt = f"""
You are an AI lead analysis assistant.

Analyze the following customer enquiry.

Customer Name:
{form_data.name}

Email:
{form_data.email}

Phone:
{form_data.phone}

City:
{form_data.city}

Interested In:
{form_data.interest}

Message:
{form_data.message}

Return ONLY valid JSON in exactly this format:

{{
    "category": "Course Inquiry",
    "priority": "High",
    "summary": "Short summary of customer requirement"
}}

Rules:

1. category should describe the customer's requirement.
2. priority must be one of:
   High
   Medium
   Low
3. summary should be short and useful.
4. Do not add markdown.
5. Return only JSON.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a professional lead analysis AI."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    result = response.choices[0].message.content

    try:
        return json.loads(result)
    except json.JSONDecodeError:
        return {
            "category": "General Inquiry",
            "priority": "Medium",
            "summary": result
        }