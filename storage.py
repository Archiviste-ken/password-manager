import json

def load_passwords():
    with open("passwords.json","r") as file:
        passwords = json.load(file)
    return passwords
    

def save_passwords(passwords):
    
    with open("passwords.json","w") as file:
        json.dump(passwords, file, indent = 4)
    
    
def add_passwords(website, username, password):
    
    passwords  = load_passwords()
    
    password = {
        "website": website,
        "username": username,
        "password": password
    }
    
    passwords.append(password)
    
    save_passwords(passwords)
    
    
        
        
    
    
    

    