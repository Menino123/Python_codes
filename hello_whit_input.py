from time import sleep

name1 = input("What's your first name? ")
name2 = input("What's your last name? ")

    
while not name1.isalpha():
    print("Please enter a valid name (letters only).")
    name1 = input("What's your first name? ")
    name2 = input("What's your last name? ")

while not name2.isalpha():
    print("Please enter a valid name (letters only).")
    name1 = input("What's your first name? ")
    name2 = input("What's your last name? ")


# Exibe os pontos
#________________________________________________________________________________
from time import sleep
for _ in range(3):
      
    for _ in range(3):
        print(".", end="", flush=True)
        sleep(1)
    
    # Apaga os pontos
    print("\r   \r", end="", flush=True)  # Retorna e "limpa" a linha

#________________________________________________________________________________


age = input("How old are you? ")


while not age.isdigit():
    print("Please enter a valid age (numbers only).")
    age = input("How old are you? ")
    
# Exibe os pontos
#________________________________________________________________________________

from time import sleep
for _ in range(3):
    
    for _ in range(3):
        print(".", end="", flush=True)
        sleep(1)

    # Apaga os pontos
    print("\r   \r", end="", flush=True)  # Retorna e "limpa" a linha

#________________________________________________________________________________

age = int(age)
bot_age = 3
difference_age = age - bot_age

if bot_age > age:
    print(f"Hello {name1} {name1}, you have {difference_age} less years difference with me!")
    
if bot_age < age:
    print(f"Hello {name1} {name2}, you have {difference_age} more years difference with me!")
