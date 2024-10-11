name = input("What's your name? ")
while not name.isalpha():
    print("Please enter a valid name (letters only).")
    name = input("What's your name? ")

age = input("How old are you? ")
while not age.isdigit():
    print("Please enter a valid age (numbers only).")
    age = input("How old are you? ")

age = int(age)
bot_age = 3
difference_age = bot_age + age

print(f"Hello {name}, you have {difference_age} years difference with me!")
