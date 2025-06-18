"""
Emails
Estimate: 30 minutes
Actual:   40 minutes
"""

email_to_name = {}
email  = input("Email: ")
while email != "":
    email_name = email.split("@")[0].title()
    confirm = input(f"Is your name {email_name}? (Y/n) ").lower()
    if confirm == 'n' or confirm == 'no':
        name = input("Name: ")
    else:
        name = email_name
    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")