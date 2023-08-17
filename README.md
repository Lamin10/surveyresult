
# Python Survey-result Data Management Script

The Python script facilitates the collection, analysis, and storage of survey data in a Google Sheets spreadsheet. This script integrates the Google Sheets API to access and manipulate data. The primary functionalities of the script include:

## Features

### Getting Survey Data:
The get_survey_data() function collects user input for survey details, including Name, Age, Gender, and Rating. It ensures that the entered Rating is not greater than 5 through input validation. If an invalid Rating is provided, the script will prompt the user to input a valid one.

### Updating Spreadsheet:
The update_sheet(name, age, gender, rating) function interacts with the Google Sheets API to append the collected survey data to a specified spreadsheet. It also provides feedback to the user about the appended data.

### Calculating Average Rating:
The calculate_average_rating() function computes the average rating of all survey participants. It retrieves the ratings from the spreadsheet, filters out non-numeric values, and calculates the average using valid ratings.

### Calculating Gender Counts:
   The calculate_gender_counts() function calculates the number of participants by gender. It analyzes the gender data from the 
   spreadsheet, counts the occurrences of each gender, and presents the results.

### Main Function:
   The main() function orchestrates the execution of the script. It calls the get_survey_data() function to gather input, then invokes 
   the update_sheet() function to store the survey data in the spreadsheet. Subsequently, it calculates the average rating using 
   calculate_average_rating() and displays it. Lastly, it calculates the participant counts by gender using calculate_gender_counts() 
   and displays those counts.

## packages installed:

+ Installed gspread and google-auth using the command: pip install gspread google-auth
  Set Up Credentials:

+ Created a creds.json file containing the Google Sheets API credentials,
  which run the Script.

+ Execute the script survey_result  using the command: python3 run.py
  Follow the prompts to input survey data: Name, Age, Gender, and Rating.
  The script will update the Google Sheets spreadsheet with the entered data and provide feedback on successful update.

### View Analysis:

+ The script will calculate and display the average rating of participants.
 It will also show participant counts by gender.
