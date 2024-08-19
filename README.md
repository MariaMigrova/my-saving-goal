# My Saving Goal

View the Live App [here](https://my-saving-goal-67787e47a60d.herokuapp.com/)

My Saving Goal is a personal finance tracking app designed to help you monitor your income, expenses, and savings progress with ease.

With intuitive input forms and automated goal calculations, it simplifies financial planning and keeps you on track to reach your savings goals.

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
    <td>Application loads without any error messages</td>
    <td>N/A</td>
    <td>No error messages displayed</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Main Menu is displayed and awaits user input</td>
    <td>N/A</td>
    <td>Welcome message and main menu are displayed; terminal is awaiting user input</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Input validation for all user inputs</td>
    <td>Invalid input (e.g., random text, incorrect format, wrong value)</td>
    <td>Invalid input is rejected, and the user is prompted to enter a valid input (covers all inputs)</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>All inputs accept upper and lowercase variations</td>
    <td>Valid inputs: 'm', 'M', 'u', 'U', etc.</td>
    <td>All valid inputs (regardless of case) are accepted and lead to the correct function</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Decision-making inputs are handled correctly</td>
    <td>User input: 'yes' or 'no'</td>
    <td>If 'yes', user is prompted to provide further details or proceed; if 'no', the application continues without changes</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Update or rejection is confirmed or handled properly</td>
    <td>User confirms or rejects changes</td>
    <td>If confirmed, changes are updated and saved; if rejected, user is prompted to re-enter details</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Summary validation is handled correctly</td>
    <td>User reviews summary and decides to proceed</td>
    <td>If confirmed, data is saved; if rejected, user is prompted again</td>
    <td>Pass</td>
  </tr>
</tbody>
</table>







