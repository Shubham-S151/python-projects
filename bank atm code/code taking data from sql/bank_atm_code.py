# importing libraries
import numpy as num
import pandas as pd

# importing data-connector (mysql-connector)
import mysql.connector
connection = mysql.connector.connect(
    host='127.0.0.1',         # e.g., 'localhost' or '127.0.0.1'
    user='root',     # your MySQL username
    password='password', # your MySQL password
    database='bank_atm'  # your database name
)
cursor=connection.cursor()
cursor.execute('select * from accounts')

# creating a login code 
def login():
    u=input('Enter your UserID :')
    pa=input('Enter your Password :')
    cursor.execute('select * from login_credits where userid=%s and pass=%s',(u,pa))
    user=cursor.fetchone()
    if user :
        cursor.execute('select * from accounts where account_id = %s',(user[0]))
        name=cursor.fetchone()
        if name:
            print(f'Welcome, {name[2]} {name[3]} to ABC Bank')
            return user[0]
        else :
            print('Account not found !')
    else:
        print('Invalid UserID or Password! Please try again.')
# creating registration code
def register():
    print('Please note that you can only register if you have a Bank account in this bank !')
    u=input('Enter new UserID :')
    p=input('Enter your Login Password :\n (Password must be upto 20 character in length)')
    # account id must be unique 
    a=int(input('Enter Your Account id :'))
    cursor.execute('insert into login_credits (account_id, userid, pass) values (%s,%s,%s)',(a,u,p))
    cursor.execute('select * from accounts where account_id = %s',(a))
    re=cursor.fetchone()
    if re:
        print(f'Congratulations {re[2]} {re[3]} you have been registered to ATM')
# creating balance inquiry code
def bal_inquiry():
    print()
# creating cash withdraw code
def cash_withdraw():
    print()
# creating code to change login password
def change_login_pass():
    print()
# creating code to change login card pin
def change_card_pin():
    print()
# creating amount transfer code
def transfer():
    print()
# creating code
def cancel(func):
    c=int(input('Do you want to cancel the process :\
                \n press 0 to continue and 1 to exit'))
    while c==1:
        print('Exiting the process !........')
        break
    else :
        func

# creating interface
print('WELCOME TO ABC BANK \n select what you want to do :')
d = {
    'operation': [
        'Cash Withdraw',
        'Balance Inquiry',
        'Transfer',
        'Change Card Pin',
        'Change Login Password',
        'New Registration'
    ],
    'Number': [1, 2, 3, 4, 5, 6]
}
opt = pd.DataFrame(d, index=['>', '>', '>', '>', '>', '>'])
print(opt)

# selecting options
def  process():
    n=int(input('Enter your choice :'))
    if n==1:
        cancel(cash_withdraw())
    elif n==2:
        cancel(bal_inquiry())
    elif n==3:
        cancel(transfer())
    elif n==4:
        cancel(change_card_pin())
    elif n==5:
        cancel(change_login_pass())
    else :
        cancel(register())

cancel(process())