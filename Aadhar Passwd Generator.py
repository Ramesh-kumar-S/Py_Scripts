import time


def counter(count):
    return Generator(int(count))

def Generator(count):
    
    SPLITTER=[]
    for i in range(count):
        NAME=input("Enter your Name :")
        DOB=input("Enter the Date of Birth :")
        NAMES_SPLITTED=NAME[:4].upper()
        DOB_SPLITTED=DOB[-4:]
        PASSWD=NAMES_SPLITTED+DOB_SPLITTED
        SPLITTER.append(PASSWD)
    decorator()
    return Printer(SPLITTER)


def decorator():
    str="*"
    for i in range(10):
        print(i*str,end="")
        
def Printer(SPLITTER):
    for i in SPLITTER:
        print("\nYour Password is : {}".format(i))
        time.sleep(1)
    decorator()




COUNT=input("Enter the Number of Passwords to be Generated :")
counter(COUNT)
