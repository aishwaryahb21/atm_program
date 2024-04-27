name=['deepu','divya','sahana']
password=["de18","di40","sa49"]
balance=[5000,10000,6000]
def withdraw(current):
    amount=int(input("How much do you want to withdraw? "))
    if amount<=balance[current]:
        balance[current]-=amount
        print('successfully withdrawn')
    else:
        print('insufficient amount')
def checkbalance(current):
    print('balance is',balance[current])
def deposit(current):
    deposit_amount=int(input("How much do you want to deposit? "))
    balance[current]+=deposit_amount
    print('successfully deposited')
def change_password(current):
    input('Enter your current password')
    new_password=input('Enter your new password')
    if new_password!=password[current]:
        password.pop(i)
        password.insert(i,new_password)
        print('password changed')
    else:
        print('password is same')
def default(current):
    print('enter correct option')
username=input('Enter your name:')
for i in range(len(name)):
    if username == name[i]:
        userpassword=input('Enter your password:')
        if userpassword == password[i]:
            while True:
                print('1.withdraw\n2.balance\n3.deposit\n4.change_password\n5.exit')
                option=int(input('Enter your option:'))
                if option==0:break
                data={1:withdraw,2:checkbalance,3:deposit,4:change_password,5:exit}
                break
                result=data.get(option,default)
                result(i)


