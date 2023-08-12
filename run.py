import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('survey-result')

def get_survey_data():
    """
    Get survey data input from user.
    """
    print("Please enter your Name")
    NAME = input("Name")
    print("Please enter your Age")
    AGE = int(input("Age"))
    print("Please enter your Gender")
    GENDER = input("Gender")
    print("Please give your Rating")
    RATING = input("Rating")
    print(f"Your name is: {NAME}, Your gender is: {GENDER}, Your age is: {AGE}, Your rating is: {RATING}")

get_survey_data()