import json


def load_passwords():
    with open("passwords.json","r") as file:
        passwords = json.load(file)
    return passwords
    

def save_passwords(passwords):
    
    with open("passwords.json","w") as file:
        json.dump(passwords, file, indent = 4)
    
    
        
        
    
    
    

    