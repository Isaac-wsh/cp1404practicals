"""
Word Occurrences
Estimate: 30 minutes
Actual:   32 minutes
"""

email_to_name = {}
email  = input("Email: ")
while email:
    email_name = email.split("@")[0].title()
    confirm = input(f"Is your name {email_name}? (Y/n) ").lower()