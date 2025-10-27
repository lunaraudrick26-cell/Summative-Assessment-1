# Exercise 3: Biography - OPTIMIZED

# Get name and hometown (no validation needed - any text OK)
name = input("Enter your name (first and last): ")
hometown = input("Enter your hometown: ")

# Get age and make sure it's a number
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        break
    print("Please enter a valid number for age.")

# Store in dictionary and print
bio = {"name": name, "hometown": hometown, "age": age}
print(f"Name: {bio['name']}\nHometown: {bio['hometown']}\nAge: {bio['age']}")