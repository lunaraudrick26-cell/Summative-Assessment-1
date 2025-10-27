# Exercise 6: Brute Force Attack - OPTIMIZED

PASSWORD = "12345"
MAX_ATTEMPTS = 5

for attempt in range(1, MAX_ATTEMPTS + 1):
    password = input("Enter the password: ")
    
    if password == PASSWORD:
        print("Access granted! Welcome.")
        break
    
    remaining = MAX_ATTEMPTS - attempt
    if remaining > 0:
        print(f"Incorrect. {remaining} attempt(s) remaining.")
    else:
        print("Maximum attempts reached. Authorities alerted!")