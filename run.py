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
    Get survey data input from user and update the Google Sheets spreadsheet.
    """
    print("Please enter your Name")
    NAME = input("Name")
    print("Please enter your Age")
    AGE = int(input("Age"))
    print("Please enter your Gender")
    GENDER = input("Gender")
    print("Please give your Rating")
    RATING = int(input("Rating"))

    return NAME, AGE, GENDER, RATING

def update_sheet(name, age, gender, rating):
    """
    Update the Google Sheets spreadsheet with survey data.
    """
    # Open the first sheet of the spreadsheet
    sheet = SHEET.get_worksheet(0)
    
    # Append the survey data to the spreadsheet
    new_row = [name, age, gender, rating]
    sheet.append_row(new_row)
    
    print(f"Your name is: {name}, Your gender is: {gender}, Your age is: {age}, Your rating is: {rating}")
    print("Survey data appended to the spreadsheet.")


def calculate_average_rating():
    """
    Calculate the average rating of all survey participants.
    """
    sheet = SHEET.get_worksheet(0)
    ratings = sheet.col_values(4)[1:] 
    ratings = [int(rating) for rating in ratings]
    average_rating = sum(ratings) / (len(ratings))
    return average_rating

def main():
    name, age, gender, rating = get_survey_data()
    update_sheet(name, age, gender, rating)

    avg_rating = calculate_average_rating()
    print(f"Average Rating of all participants: {avg_rating}")


if __name__ == "__main__":
    main()  
 