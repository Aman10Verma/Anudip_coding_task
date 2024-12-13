# Write a python program to check if a string is a valid email address.
# Take input from the user
email = input("Enter an email address: ")
# Check if the email contains exactly one '@' symbol
if email.count('@')==1:
    # Split the email into username and domain parts
    username, domain=email.split('@') # Divide the email into two parts
    # Check if the username and domain is not empty
    if username and domain: #Ensure both parts are present
        if '.' in domain and len(domain.split('.')[-1])>=2: # Check for a valid format
            print("Valid email address.")
        else:
            print("Invalid email address: Missing or invalid domain.") #Error message for the domain issues
    else:
        print("Invalid email address: Missing username or domain.") # Error message for the missing parts
else:
    print("Invalid email address: Must contain one '@'.") # Error message for '@' count issue 