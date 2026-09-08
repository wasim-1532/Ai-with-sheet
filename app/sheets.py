import os
import gspread

from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

load_dotenv()


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


def get_sheet():

    credentials_file = os.getenv(
        "GOOGLE_CREDENTIALS_FILE"
    )

    credentials = Credentials.from_service_account_file(
        credentials_file,
        scopes=SCOPES
    )

    client = gspread.authorize(credentials)

    sheet_name = os.getenv("GOOGLE_SHEET_NAME")

    spreadsheet = client.open(sheet_name)

    worksheet = spreadsheet.sheet1

    return worksheet


def add_lead(form_data, ai_data):

    worksheet = get_sheet()

    row = [
        form_data.name,
        form_data.email,
        form_data.phone,
        form_data.city,
        form_data.interest,
        form_data.message,
        ai_data["category"],
        ai_data["priority"],
        ai_data["summary"]
    ]

    worksheet.append_row(row)

    return True