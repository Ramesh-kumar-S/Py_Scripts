import time

#Fucntion Passes the Count of Number of Mail Id's to be Genrated
def emailgenerator(count):
    c=count
    return gen(count)


#Fuction generates E-Mails
def gen(count):
    MAILBOX=[]
    for i in range(count):
        NAME_SPACED= input("Enter your Name :").lower().split()
        NAME="".join(NAME_SPACED)
        INITIAL=input("Enter your Initial :").lower()
        BATCH_FULL=input("Enter your Batch :")
        BATCH=BATCH_FULL[-2:]
        DEPT=str(input("Enter you Department :")).lower()
        DOMAIN=input("Enter the Domain  Name Given by your E-Mail Provider :").lower()
        TLD=input("Enter your TLD Name : ").lower()
        email=str(NAME)+str(INITIAL)+"."+str(BATCH)+str(DEPT)+"@"+DOMAIN+"."+TLD
        MAILBOX.append(email)
        REMAINING=int(count)-int(i+1)
        print("{} Mail Id's to be Genrated".format(REMAINING))
        time.sleep(2)
    return mailprinter(MAILBOX)


#Fucntion Prints the  Generrated Mail Id's
def mailprinter(MAILBOX):
    count=0
    st="*"
    for i in range(10):
        time.sleep(1)
        print(i*st,end='')
    print("\nGenerating E-Mail's...")
    for i in MAILBOX:
        time.sleep(1)
        count += 1
        print("{0} . {1} ".format(count,i))

#Driver Code
NO=int(input("Enter the No of Emails to be Generated :"))
emailgenerator(NO)