import random
import json
import logging

logging.basicConfig(filename="transactions.log", level=logging.INFO, format='%(asctime)s >>  %(message)s ')

def read_users():
    global list_of_users
    list_of_users=[]
    with open("users.json") as f:
        u_data = json.load(f)
        list_of_users = u_data["customers"]
            

read_users()            #Accesing old users from users.json


class User:
    
    def __init__(self, card_no, PIN, balance):   #Registration
        self.card_no=card_no
        self.PIN=PIN
        self.balance=balance

    def authentication(self, cardno):               #If card number in database authenticate with PIN
        self.cno = cardno
        if self.cno==self.card_no:
            self.pin=int(input("Enter 4 digit PIN:"))
            if self.pin==self.PIN:
                print("\n\t\t\tYou are signed in.\n" )
                self.operations()
                t2=True
                while(t2):
                    res=input("Sign Out [y/n]:")
                    if res=='y':
                        print("ThankYou for using our services")
                        t2=False
                    else:
                        print("\n")
                        self.operations()
            else:
                print("Incorrect Pin!!")
        else:
            print("Enter valid card number!!")
    
    def operations(self):                   #If PIN is correct, operating account
        t=True
        while(t):
            ans=int(input("Please choose from below options:\n" "\t1.Withdraw\n" "\t2.Deposit\n" "\t3.Show balance" "\nYour choice:"))
            if ans==1:
                print("\n")
                self.withdraw()
                t=False
            elif ans==2:
                print("\n")
                self.deposit()
                t=False
            elif ans==3:
                print(self.balance)
                print("\nThankyou for using our services")
                t=False
            else:
                print("\nEnter valid option!!")
            

    def withdraw(self):                         
        t=True
        while(t):
            self.amount=float(input("Enter amount to be withdrawn:"))
            if(self.amount>self.balance):
                print("\nInsufficient Balance!!")
                print("\nDeposit Money?[y/n]")
                ch=input("Enter Response:")
                if ch=='y':
                    print("\n")
                    self.deposit()
                else:
                    continue
            else:
                self.balance = self.balance - self.amount
                print("\nWithdrawl successful\nPlease collect your cash\n")
                with open("users.json") as f:
                    change_bal=json.load(f)
                    l=change_bal["customers"]
                    for i in range(len(l)):
                        if(l[i]["cardno"]==self.card_no):
                            l[i]["balance"]=self.balance
                with open("users.json","w") as f:
                    json.dump(change_bal, f, indent=4)
                read_users()
                logging.info("{} amount has been deducted from bank a/c with card number : {}\n".format(self.amount, self.card_no))
                p=input("Show Balance? [y/n]:")
                if p=='y':
                    print(self.balance ) 
                    print("\n")
                t=False
    
    def deposit(self):
        self.amount=float(input("Enter amount to be deposited:"))
        self.balance+=self.amount
        print("\nCash deposited successfully")
        with open("users.json") as f:
            change_bal=json.load(f)
            l=change_bal["customers"]
            for i in range(len(l)):
                if(l[i]["cardno"]==self.card_no):
                    l[i]["balance"]=self.balance
        with open("users.json","w") as f:
                    json.dump(change_bal, f, indent=4)
        read_users()
        logging.info("{} amount has been deposited from bank a/c with card number : {}\n".format(self.amount, self.card_no))
        p=input("Show Balance? [y/n]:")
        if p=='y':
            print(self.balance)
            print("\n")

def new_user():
    name = name2=input("Enter Name:")
    usercardno=random.randint(1000000000000000,9999999999999999)
    while(True):
        userpin=int(input("Set your 4 digit PIN:"))
        if(999<userpin<10000):
            continue
        else:
            break
    name = User(usercardno, userpin, 0)
    user_data={"name":name2, "cardno":usercardno, "pin":userpin, "balance":0}
    list_of_users.append(user_data)
    with open("users.json","r") as f2:
        users2=json.load(f2)
        users2["customers"].append(user_data)
    with open("users.json", "w") as f3:
        json.dump(users2, f3, indent=4)
    print("Account with Card number: "+str(usercardno)+" PIN:"+str(userpin)+" has been created successfully\n")


def ATMprocess():
    while(True):       
        print("1.New User\n2.Existing User")
        response=int(input("Your Response:"))
        if response==1:
            print("\n")
            new_user()
        else:
            #print("\n")
            while(True):
                cardno = int(input("\nEnter Card number:"))
                for d in list_of_users:
                    if d['cardno']==cardno:
                        print("\n\t\tWelcome User with card number "+str(cardno)+"\n")
                        old_user=User(cardno, d['pin'], d['balance'])
                        old_user.authentication(cardno)
                        break
        ans=input("Exit[y/n]:")
        if ans=='y':
            print("ThankYou for using our services")
            break
        else:
            print("\n")
            continue

ATMprocess()