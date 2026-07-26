# from storage import add_passwords, view_websites, search_password, delete_password
# from password_utils import generate_password

# add_passwords("github.com", "shreyesh", "abc123")
# print("Yo, homie, your password is added!!!")

# print("\n")

# view_websites()

# search_password("github.com")

# delete_password(1)

# password = generate_password(12)

# print(password)

# ========== Password Manager ==========

# 1. Add Password
# 2. View Websites
# 3. Search Password
# 4. Delete Password
# 5. Generate Strong Password
# 6. Exit

from password_utils import generate_password
from storage import add_passwords, view_websites, search_password, delete_password


while True:
    
    print("""
========== Password Manager ==========

1. Add Password
2. View Websites
3. Search Password
4. Delete Password
5. Generate Password
6. Exit
""")
    
    choice = input("Choose an option!!!")
    
    if choice == "1":
        
        try:
            website = input("Website: ")
            username = input("Username: ")
            generate = input("Generate Password Automatically? (Y/N): ").strip().upper()
            if generate == "Y":
                length = int(input("Password Length: "))
                password = generate_password(length)
                print(f"\nGenerated Password: {password}")
                    
                    
            elif generate == "N":
                password = input("Enter Password: ")
                        
            else:
                print("Invalid choice.")
                continue
                    
            add_passwords(website, username, password)
                    
            print("Password Saved Successfully ✅")
            
        except ValueError:
            print("Please enter valid input")
        
        
    elif choice == "2":
        view_websites()
        
    elif choice == "3":
        website = input("Enter website name to search")
        search_password(website)
        
    elif choice == "4":
        try:
            view_websites()
            index = int(input("Enter website number to delete:"))
            delete_password(index)
            
        except ValueError:
            print("Please enter valid input")
            
    
    elif choice == "5":
        try: 
            length = int(input("Enter Password Length: "))
            password = generate_password(length)
            print("\n========== Generated Password ==========")
            print(password)
            
        except ValueError:
            print("Please enter valid input")
        
    elif choice == "6":
        print("Sayonara!!!")
        break

    else:
        print("Invalid choice.")
        
    
    input("\n Press enter to continue..... ")
    
    