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
    NAME = str.capitalize(input("Name:\n "))
    print("Please enter your Age")
    AGE = int(input("Age:\n "))
    print("Please enter your Gender:")
    GENDER = str.capitalize(input("Gender:\n "))
    print("Please give your Rating")
    while True:
        try:
            RATING = int(input("Rating: "))
            if RATING > 5:
                raise ValueError("Rating cannot be greater than 5")
            break  # Exit the loop if valid rating entered
        except ValueError:
            print("Rating cannot be greater than 5")
            print("Invalid rating. Please enter a valid rating.")
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
    
    # Filter out non-numeric values and empty strings from ratings
    valid_ratings = [int(rating) for rating in ratings if rating.isdigit()]
    
    if not valid_ratings:
        return 0  # No valid ratings
    
    average_rating = sum(valid_ratings) / len(valid_ratings)
    return average_rating

def calculate_gender_counts():
    """
    Calculate the counts of participants by gender.
    """
    sheet = SHEET.get_worksheet(0)
    genders = sheet.col_values(3)[1:] 
    gender_counts = {gender: genders.count(gender) for gender in set(genders)}
    return gender_counts

def main():
    name, age, gender, rating = get_survey_data()
    update_sheet(name, age, gender, rating)

    avg_rating = calculate_average_rating()
    print(f"Average Rating of all participants: {avg_rating}")

    gender_counts = calculate_gender_counts()
    print("Participant Counts by Gender:")
    for gender, count in gender_counts.items():
        print(f"{gender}: {count}")


if __name__ == "__main__":
    main()  
 