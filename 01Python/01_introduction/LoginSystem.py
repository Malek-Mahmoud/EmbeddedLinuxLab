#!/usr/bin/python3

def Verify_Login(Username,Password,Credentialfile):
    Password = Password + "\n"

    file = open(Credentialfile,'r')
    lines = file.readlines()
    for line in lines:
        fields = line.split(',')
        
        if(fields[0] == Username and fields[1] == Password):
            return True
    
    return False        


for i in range(3):
    username = input("Username: ")
    password = input("Password: ")
    if(Verify_Login(username,password,"Credential.txt") == True):
        print(f"Welcome {username}")
    else:
        print("Invalid username or password")    
