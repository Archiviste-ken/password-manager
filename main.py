from storage import add_passwords, view_websites, search_password, delete_password

add_passwords("github.com", "shreyesh", "abc123")
print("Yo, homie, your password is added!!!")

print("\n")

view_websites()

search_password("github.com")

delete_password(1)