email=input("Enter the E-Mail ID: ")

#Function Check Whether it's an Valid Email or Not
def validator(email):
    valid_mail=False
    for i in email:
        if i=="@":
            valid_mail=True
            break
    return valid_mail

#Validator Driver Code

VALIDATER = validator(email)

#Function to Count Dot Characters in an E-Mail

def dotdetector(email):
    MESSENGER=''
    count=0
    for i in email:
        if i=='.':
            count +=1
    if count >= 2:
        MESSENGER=dottedmail(email)                   
    else:
        MESSENGER=ordinarymail(email)
    return MESSENGER
                   
def dottedmail(email):
    splitter=[]
    splitter=email.split('.')
    return splitter[-1]
    
def ordinarymail(email):
    splitter=[]
    splitter=email.split('.')
    return splitter[-1]
 
#Main Driver Code
    
dotdetector(email) 
 
#Enter the Condition If It's Only an Valid E-Mail

if VALIDATER==True:
    index_of_at=email.index("@")
    domain=email[index_of_at+1:index_of_at+6]
    
    TLD=dotdetector(email)                  #Access the Function to Detect the Number of Dot Characters in an E-mail
    
    print("Username :",email[:index_of_at])
    if domain=="gmail":
        print("Domain is : G-Mail")
    elif domain=="yahoo":
        print("Domain is : Yahoo Mail")
    else:
        print("Custom Domain : ",domain)

    if TLD=="com":
        print("Top Level Domain is : Dot-Com(.Com)")
    elif TLD=="edu":
        print("Top Level Domain is : Educational Institution Domain(.Edu)")
    elif TLD=="org":
        print("Organizational E-Mail(.Org)")
    else:
        print("Seems like Customised TLD")
else:
    print("Enter Valid Mail!!")



