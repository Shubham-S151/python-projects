# this code is currently incomplete

# Bank atm code
## Overview
This project is a simple bank login page implemented in Python. It allows users to log in, register, check their balance, withdraw cash, and change their password using data stored in an Excel file.

## Features
- User login and registration
- Cash withdrawal
- Balance inquiry
- Change card password
## Requirements
- Python 3.x
- pandas library
- numpy library
- An Excel file containing sample bank data
  -Sample Data Structure
    - The Excel file should have the following columns:
      - username
      - password
      - firstname
      - lastname
      - accnum (account number)
      - balance
You can create a sample Excel file named sample data for bank login code.xlsx with the necessary data in your specified directory.

## Installation
### Clone the repository:

- Copy code
git clone <repository-url>
### Install the required libraries:

- Copy code
pip install pandas numpy openpyxl
## Usage
1. Make sure to update the path to your Excel file in the script:

df = pd.read_excel(r"C:\Users\HP\Desktop\bank atm code\sample data for bank login code.xlsx")

2. Run the script:

atm code.py

3. Follow the prompts to log in or register a new account.

## Code Explanation
Here’s a brief explanation of the code functionality:

- Data Import: The bank data is loaded from an Excel file using the pandas library.
- Login and Registration: Users can log in with their username and password. If they are not registered, they can register - directly through the prompt.
- Banking Operations: Users can choose from several operations:
  - Cash withdrawal
  - Balance inquiry
  - Change card password
- Data Persistence: The code currently updates the DataFrame in memory but does not save changes back to the Excel file. You can extend the functionality to save the updated DataFrame.
## Example Usage
When prompted, you can enter your username and password. If they match the records, you'll be welcomed and given options for banking operations.

WELCOME TO ABC BANK 
 select what you want to do :
 {'cash withdraw': 1, 'balance inquiry': 2, 'transfer': 3, 'change card password': 4, 'new registration': 5}
## Future Enhancements
- Implement data persistence to save updates back to the Excel file.
- Add error handling for invalid inputs.
- Enhance security features, such as password hashing.
## License
This project is open-source and available under the MIT License.
