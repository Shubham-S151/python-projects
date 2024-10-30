# bank atm code
# create a sample bank data for this code and import it into python 
import pandas as pd
import numpy as num
df=pd.read_excel(r"C:\Users\HP\Desktop\bank atm code\sample data for bank login code.xlsx")

fn=df['firstname'].values[0]
ln=df['lastname'].values[0]
acc=df['accnum'].values[0]
bl=df['balance'].values[0]
# creating a function to check user authentication
def loginandregis():
    u=input('enter your user_name :')
    p=int(input('enter your password :'))
    if (u.lower() in df['username'].str.lower().values) and (p in df['password'].values):
        first_name = df['firstname'].values[0]
        last_name = df['lastname'].values[0]
        print(f'Welcome, {first_name} {last_name}')
        return True
    else :
        print('access denied \neither usernme or password mismatched \
            \n if you are not registered then please register yourself')
        q=int(input('Do you want to register? If yes, enter 1; else enter 0: '))
        if q==0:
            print('Exiting the registration process.')
            return False
        else :
            u1=input('enter user name :')
            p1=int(input('enter password :'))
            f=input('enter first name :')
            l=input('enter last name :')
            b=int(input('enter your curent balance :'))
            df.loc[len(df)] = [u1,p1,f,l,b]
            print('Registration successful!')
            return False
            

# code starts
print('WELCOME TO ABC BANK \n select what you want to do :')
d={'operation':['cash withdraw',
   'balance inquiry',
   'transfer',
   'change card password',
   'new registration'],'number':[1,2,3,4,5]}
opt=pd.DataFrame(d,index=['*','*','*','*','*'])
print(opt)
a=int(input('select the option below :'))
if a==1:
    print('cash withdraw')
    print('confirm process :')
    b=int(input('enter 0 for no and 1 for yes :'))
    if b==1:
        if loginandregis():
            amt=int(input('enter your amount :'))
            df['balance']=df['balance'].values[0]-amt
            print('Transaction Sucessfull!')
elif a==2:
    print('balance inquiry')
    if loginandregis():
        print(f'hello {fn} {ln},\nyour account balance for {acc} is {bl}')
elif a==3:
    print('change card password')
    if loginandregis():
        op=int(input('enter old password'))
        i=df[df['password']==op].index()
        np=int(input('enter new password :'))
        df['password'][i]=np
elif a==4:
    print('new registration')
    print('for new users please type 0 and 0 in the next questions')
    loginandregis()
else:
    print('TRANSACTION ABORTED')
