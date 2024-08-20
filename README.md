# My Saving Goal

View the Live App [here](https://my-saving-goal-67787e47a60d.herokuapp.com/)

My Saving Goal is a personal finance tracking app designed to help you monitor your income, expenses, and savings progress with ease.

Set your own savings goal with a target amount and date, and update it anytime as your financial plans evolve. The app integrates with Google Sheets, where all your income and expense data are securely stored. Previous inputs are saved, allowing you to build on your existing financial history, and your savings are updated accordingly. (GoogleSheetsLink.txt)

Stay organized and in control of your finances with real-time updates and progress tracking.

## User Expectations
### Ease of Use
- Users expect a simple and intuitive interface that allows them to effortlessly input their incomes and expenses or update their saving goal. The app should provide clear prompts and easy navigation to guide users through the process.

### Accurate Calculations
- Users expect the app to accurately track their savings, ensuring that all calculations based on the entered data are precise. Real-time updates and summaries of the savings and expenses should be presented to the user.

### Goal Tracking
- Users expect helpful insights into their progress toward their financial goals. This includes calculations showing how much needs to be saved on a weekly basis to stay on track.

### Data Security
- Users expect their personal and financial data to be stored securely, ensuring privacy and confidentiality. Only the user should have access to their data.

## Flow Chart

This flow chart provides a high-level overview of how the application operates and helps in understanding the flow of data and user interactions. 

![FlowChart](https://github.com/user-attachments/assets/598852ab-eaa6-4368-90e6-e1f5edb0501d)

## Features

### Start of the App

User gets a Welcome Message in a nice format.

![image](https://github.com/user-attachments/assets/9fbed67e-112e-4ed3-9d75-f387a3c397c8)

### Goal Update

User gets an option to update his savings goal. 

![image](https://github.com/user-attachments/assets/652b20d1-b44f-45d3-a27e-415c20befb09)

### Incomes and Expenses Tracking

#### Input Forms

Easily add new incomes and expenses with intuitive input forms.

![image](https://github.com/user-attachments/assets/392556ce-b5b6-42de-a94a-8047bb80eea8)

#### Categories

Organize your financial entries by categories such as Wages, Freelance, Housing, Transport, and more.

![image](https://github.com/user-attachments/assets/05cbbd00-3904-4349-ba30-20e36b70bdc3)

### Savings Summary

#### Comprehensive Overview

Displays a detailed summary of your total income, expenses, and current savings.

![image](https://github.com/user-attachments/assets/ee11b89c-7b3c-48fa-999d-ed6027a6be75)
  
#### Date and Week Tracking

Keeps track of financial data by date and week number for better organization.

![image](https://github.com/user-attachments/assets/3a8197b4-664d-488b-a208-93d19d07eadc)

### Goal Setting and Progress Tracking

Calculates how much more you need to save to reach your goal and estimates the average weekly savings required.

![image](https://github.com/user-attachments/assets/91acd71d-3dac-4c61-bd47-267bda81ec2f)

### Final Message

Final thank you message

![image](https://github.com/user-attachments/assets/8767b0d0-06bc-4676-9d19-cffc001a7c2d)

## Technologies Used

- Python: Core programming language used to build the application's logic.
  
- GitHub: For version control, code storage, and collaboration.
  
- Gitpod: Cloud-based development environment used for coding and testing.
  
- Heroku: Platform used for deploying and hosting the application online.
  
- LucidCharts: Tool for designing flowcharts and diagrams to map out project logic
  
- CI - Python Linter: Automated tool used to ensure code quality and consistency.
  
- Google Sheets: Used to store and manage user data for the application.
  
- Google Cloud: Platform for accessing APIs and managing cloud resources.

### Python Libraries

- Gspread: A library used to interact with Google Sheets, enabling reading and writing of data programmatically.

- Credentials from google.oauth2.service_account: Used for authentication and authorization with Google APIs using service account credentials.

- Datetime: Standard Python library used to work with dates and times, including parsing, formatting, and manipulating date-related data.

## Testing

### Validator Testing

I used Code Institute’s Python Linter to validate my Python code, ensuring it adheres to best practices. No errors were found during validation.

![image](https://github.com/user-attachments/assets/0e696085-427d-4d58-b5cd-a2f47218423f)

### Manual Testing


<table>
<thead>
  <tr>
    <th>Test Case</th>
    <th>Input Scenario</th>
    <th>Actual Result</th>
    <th>Pass / Fail</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Application Loads without Any Error Messages</td>
    <td>N/A</td>
    <td>No error messages displayed</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Welcome Message Displayed</td>
    <td>N/A</td>
    <td>Welcome message displayed and awaiting user input</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Goal Update Confirmation - Yes/No</td>
    <td>Invalid Input (e.g., random word)</td>
    <td>Displays invalid input message and prompts user for correct input</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Saving Goal Amount Input</td>
    <td>Invalid Input (e.g., letters)</td>
    <td>Displays invalid input message and prompts user for correct input</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Saving Goal Date Input</td>
    <td>Invalid Input (e.g., incorrect format or past date)</td>
    <td>Displays invalid input message and prompts user for correct input</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Save Updated Goal - Yes/No</td>
    <td>Invalid Input (e.g., random word)</td>
    <td>Displays invalid input message and prompts user for correct input</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Add New Income - Yes/No</td>
    <td>Invalid Input (e.g., random word)</td>
    <td>Displays invalid input message and prompts user for correct input</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Income Date Input</td>
    <td>Invalid Input (e.g., incorrect format, future date, or date older than 3 months)</td>
    <td>Displays invalid input message and prompts user for correct input</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Income Type Input</td>
    <td>Invalid Input (e.g., number not in list or letters)</td>
    <td>Displays invalid input message and prompts user for correct input</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Income Amount Input</td>
    <td>Invalid Input (e.g., letters or amount exceeding 1,000,000)</td>
    <td>Displays invalid input message and prompts user for correct input</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Save Income - Yes/No</td>
    <td>Invalid Input (e.g., random word)</td>
    <td>Displays invalid input message and prompts user for correct input</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Add Another Income?</td>
    <td>Invalid Input (e.g., random word)</td>
    <td>Displays invalid input message and prompts user for correct input</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Add New Expenses - Yes/No</td>
    <td>Invalid Input (e.g., random word)</td>
    <td>Displays invalid input message and prompts user for correct input</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Expenses Date Input</td>
    <td>Invalid Input (e.g., incorrect format, future date, or date older than 3 months)</td>
    <td>Displays invalid input message and prompts user for correct input</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Expenses Type Input</td>
    <td>Invalid Input (e.g., number not in list or letters)</td>
    <td>Displays invalid input message and prompts user for correct input</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Expenses Amount Input</td>
    <td>Invalid Input (e.g., letters or amount exceeding 1,000,000)</td>
    <td>Displays invalid input message and prompts user for correct input</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Save Expenses - Yes/No</td>
    <td>Invalid Input (e.g., random word)</td>
    <td>Displays invalid input message and prompts user for correct input</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Add Another Expense?</td>
    <td>Invalid Input (e.g., random word)</td>
    <td>Displays invalid input message and prompts user for correct input</td>
    <td>Pass</td>
  </tr>
</tbody>
</table>



## Deployment

### How to Deploy the Project

#### 1. Create a Heroku Account and Log In:

- If you don’t already have a Heroku account, sign up at Heroku. Log in if you have an existing account.

#### 2. Create a New App:

- Go to your Heroku dashboard and click on “New,” then select “Create new app.”
  
- Provide a name for your app and choose a region, then click on “Create app.”
  
#### 3. Configure Settings:

- Navigate to the “Settings” tab at the top of the page.
  
- Under “Config Vars,” set your Key/Value pairs as needed.
  
#### 4. Add Buildpacks:

- In the “Buildpacks” section, add the required buildpacks in the following order:
  
  - Click the Python icon and select “Add Buildpack.”
  - Next, click the Node.js icon and select “Add Buildpack.”

#### 5. Set Up Deployment:

- Go to the “Deployment” tab.

- Under “Deployment method,” choose “GitHub” if your repository is hosted there.

- In the “Connect to GitHub” section, find your repository and click “Connect.”

- To enable automatic deployments, click “Enable Automatic Deploys.” For a one-time deployment, go to the “Manual Deploy” section and click “Deploy Manually.”

### How to Clone the Project

#### 1. Log into GitHub:

- Visit GitHub and log in to your account.
  
#### 2. Navigate to the Project Repository:

- Go to the repository at (https://github.com/MariaMigrova/my-saving-goal).
  
#### 3. Copy the Repository Link:

- Click the “Code” button and copy your preferred link (either HTTPS or SSH).
  
#### 4. Clone the Repository:

- Open the terminal in your code editor.
  
- Change the working directory to the location where you want to clone the repository.
  
- Type git clone followed by the link you copied and press Enter.

### How to Fork the Repository 
#### 1. Log into GitHub:

- Visit GitHub and log in to your account.

#### 2. Navigate to the Project Repository:

- Go to the repository at (https://github.com/MariaMigrova/my-saving-goal).

#### 3. Fork the Repository:

- Click the “Fork” button in the top right corner of the page.

## Credits and References

- **API Creation, Encryption Key, and Google Cloud Integration:**  
  This project utilizes concepts and techniques from the Code Institute: "Love Sandwiches" project.

- **Readme File Guidance:**  
  Inspiration for this README file was drawn from the [README.md](https://github.com/bmays9/top-trumps/blob/main/README.md) of the Top Trumps project by [bmays9](https://github.com/bmays9).

- **Special Thanks:**  
  A special thank you to my mentor, Harry Dhillon, for his invaluable support and guidance. His advice has been incredibly valuable and deeply appreciated throughout this project.







