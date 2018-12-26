#Final Project

import csv
import os

'''
=============================================
Define the account class and all methods
=============================================
'''

class Account():

    def __init__(self, name = 'myAccount', balance = 0, monthlyCreditSums = {}, monthlyDebitSums = {}):
        self.name = name #Name of Account
        self.balance = round(float(balance), 2) #Balance of Account
        self.monthlyCreditSums = monthlyCreditSums #sum of earnings each month
        self.monthlyDebitSums = monthlyDebitSums #sum of spendings each month

    def __repr__(self):
        return 'Account(name=%s, balance=%s, monthlyCreditSums=%s, monthlyDebitSums=%s)' % \
                (self.name, self.balance, self.monthlyCreditSums, self.monthlyDebitSums)

    def getAccountName(self): #get name of account
        return self.name

    def setAccountName(self, name): #set name of account
        self.name = name

    def getBalance(self): #get current balance of account
        return self.balance

    def setBalance(self, balance): #set current balance of account
        self.balance = round(float(balance),2)

    def getMonthlyCreditSums(self): #get all monthly amounts earned
        return self.monthlyCreditSums

    def setMonthlyCreditSums(self, creditSums): #set all monthly earnings
        self.monthlyCreditSums = creditSums

    def getMonthlyDebitSums(self): #get all monthly spending
        return self.monthlyDebitSums

    def setMonthlyDebitSums(self, debitSums): #set all monthly spendings
        self.monthlyDebitSums = debitSums

    '''
    ============================================
    Function: uploadFile
    Upload the transaction history
    ============================================
    '''

    def uploadFile(self):

        fileName = input('Please enter file name: ')
        if os.path.isfile(fileName): #if file exists
            inFile = open(fileName, 'r')
            transactionFile = csv.reader(inFile, delimiter=',') #load and separate transactions

            transactions = [] #place all transactions into list
            next(transactionFile) #skip header because it's not a txn

            '''Retrieve month summaries and current balance
            So that we can edit them in this new upload of txns
            '''
            monthDebitSums = self.getMonthlyDebitSums()
            monthCreditSums = self.getMonthlyCreditSums()
            currentBalance = self.getBalance()

            for row in transactionFile:

                '''
                Placement of data in txn file
                row[0] = date
                row[1] = Description
                row[2] = AmountDebit
                row[3] = amount credit
                '''

                '''Get month and year of txn
                    i.e. remove the day since we don't need that
                '''
                date = row[0].split('/')
                month = date[0] + '/' + date[2]

                if row[2] == "": #if cell is blank, make it zero
                    row[2] = 0

                if row[3] == "":
                    row[3] = 0

                if month in monthDebitSums:
                    monthDebitSums[month] += float(row[2])
                    monthCreditSums[month] += float(row[3])

                else:
                    monthDebitSums[month] = float(row[2])
                    monthCreditSums[month] = float(row[3])

                '''Add to account balance'''
                currentBalance = currentBalance + float(row[2]) + float(row[3])

            self.setBalance(currentBalance)

            inFile.close()

        else: #if file does not exist
            print('')
            print('File Not Found. Please enter a new file name.')
            print('Type Menu to return to main menu.')


    def outputTotals(self):

        '''
        ===========================================
        Print to master output file
        1. read file and save data. close file
        2. write file
        ===========================================
        '''

        outFileName = self.getAccountName() + ' monthTotals.csv'
        outFile = open(outFileName, 'w')
        masterFile = csv.writer(outFile, delimiter=',')

        headerRow = ['Month', 'Total Spend', 'Total Earned', 'Net Sum']
        masterFile.writerow(headerRow)

        yearSpend = 0
        yearEarned = 0

        monthDebitSums = self.getMonthlyDebitSums()
        monthCreditSums = self.getMonthlyCreditSums()

        for month in monthDebitSums:
            yearSpend += monthDebitSums[month]
            yearEarned += monthCreditSums[month]
            netSum = monthCreditSums[month] - monthDebitSums[month]
            row = [month, monthDebitSums[month], monthCreditSums[month], netSum]
            masterFile.writerow(row)

        '''Print the final row with year total'''
        footerRow = ['Total', yearSpend, yearEarned, yearEarned + yearSpend]
        masterFile.writerow(footerRow)

        outFile.close()

        print('Monthly Totals Exported to "', outFileName, '"')


'''
============================================
save/load:
============================================
'''

def loadAccounts():

    accounts = []

    if os.path.isfile('allAccounts.csv'): #if file exists
        inFile = open('allAccounts.csv', 'r')
        accountsFile = csv.reader(inFile, delimiter=',')

        next(accountsFile)
        for row in accountsFile:
            accounts.append(row)

        inFile.close()

    else:
        outFile = open('allAccounts.csv', 'w')
        masterFile = csv.writer(outFile, delimiter=',')

        headerRow = ['Account Name', 'Current Balance']
        masterFile.writerow(headerRow)

        outFile.close()

    return accounts

def saveProgram(accounts):

    outFile = open('allAccounts.csv', 'w')
    masterFile = csv.writer(outFile, delimiter=',')

    headerRow = ['Account Name', 'Current Balance']
    masterFile.writerow(headerRow)

    for account in accounts:
        row = [account[0], account[1]]
        masterFile.writerow(row)

    outFile.close()


'''
============================================
Main:
Will keep the menu open and call functions from above
============================================
'''

def main():

    print('')
    print('Welcome to the program')
    print('')

    myAccount = None
    accounts = loadAccounts()

    runProgram = True
    while runProgram:

        accountNumber = 0

        menuTwo = False

        print('')
        print('1. Create a new account')
        print('2. Load an existing account')
        print('3. Quit')
        print('')

        try:

            selection = eval(input('Please make a selection: '))

        except Exception as e:
            print('Not a valid input. Please try again.')
            print('')

        if selection == 1:
            accountName = input('Enter Account Name: ')
            balance = input('Enter starting balance: ')
            myAccount = Account(accountName, balance)
            accounts.append([myAccount.getAccountName(), myAccount.getBalance()])
            accountNumber = accounts.index(accounts[-1])
            menuTwo = True

        elif selection == 2:
            if len(accounts) == 0:
                print('No existing accounts')
                print('')

            else:
                i = 0
                for account in accounts:
                    print('Account Number:', i)
                    print('Account Name:', account[0])
                    print('Account Balance:', account[1])
                    print('')
                    i += 1
                accountNumber = eval(input('Which account number would you like to load? '))
                myAccount = Account(accounts[accountNumber][0],accounts[accountNumber][1])
                menuTwo = True

        elif selection == 3:
            print('Now exiting the program.')
            saveProgram(accounts)
            menuTwo = False
            runProgram = False

        else:
            print('Please choose a number from the options above.')

        while menuTwo:

            print('')
            print('Current Selected Account is:', myAccount.getAccountName())
            print('Current Balance is:', myAccount.getBalance())
            print('')
            print('1. Upload New Transaction History')
            print('2. Edit Account name')
            print('3. Edit Current Balance')
            print('4. Export Account Summary')
            print('5. Save and Back to Main Menu')
            print('')

            try:

                selection = eval(input('Please make a selection: '))

                if selection == 1:
                    myAccount.uploadFile()

                elif selection == 2:
                    newName = input('What is the account name? ')
                    myAccount.setAccountName(newName)

                elif selection == 3:
                    newBalance = eval(input('What is the current balance? '))
                    myAccount.setBalance(newBalance)

                elif selection == 4:
                    myAccount.outputTotals()

                elif selection == 5:
                    accounts[accountNumber] = [myAccount.getAccountName(), myAccount.getBalance()]
                    menuTwo = False

                else:
                    print('Please choose a number from the options above.')

            except Exception as e:
                print('Not a valid input. Please try again.')



main()
