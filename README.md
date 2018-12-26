# Personal Finance Tracker

A Python program which allows the user to log purchases and income and will export a monthly summary of totaly amount spent and earned. User can keep track of multiple accounts (personal, work, etc.) and keep track of currentt balance and overview of each account. 

### Prerequisites

Python 3

### Compiling

```
python3 personal-finance-tracker.py
```

## Testing

1. Upon compiling, main menu will appear with three options:
```
1. Create a new account
2. Load an existing account
3. Quit
```

2. Type `1` and press ENTER to create a new account
3. Enter an account name and a starting balance. Note: Starting balance is the initial balance at the time you will begin logging your transactions.
4. Account Menu will appear with 5 options:
```
1. Upload new Transaction History
2. Edit Account Name
3. Edit Current Balance
4. Export Account Summary
5. Save and Back to Main Menu
```

5. Press `1` and ENTER to upload a new list of transactions.
6. Enter the file name of transactions. Three CSV example files are provided here to work with. Format of file must include Date, Description, Amount Spent (as negative) and Amount Earned.
7. After transactions are loaded, balance will be updated an account menu.
8. Press `4` and ENTER to export account summary. A CSV file will be exported labeled `[Account Name] monthTotals.csv`. File will contain a summary of amount spent/earned per month.
9. Make sure to select Save and Back to Main Menu to save changes.

