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
    
def view_websites():

    passwords = load_passwords()

    if not passwords:
        print("No websites listed!!!")
        return

    print("========== Saved Websites ==========")

    for index, password in enumerate(passwords, start=1):
        print(f"{index}. {password['website']}")
        print("-" * 25)

    print(f"Total Websites: {len(passwords)}")
    
    
def search_password(website):

    passwords = load_passwords()

    for password in passwords:

        if password["website"].lower() == website.lower():

            print("\n========== Password Found ==========\n")
            print(f"Website : {password['website']}")
            print(f"Username: {password['username']}")
            print(f"Password: {password['password']}")

            return

    print("Password Not Found.")