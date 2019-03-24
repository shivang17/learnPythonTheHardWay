print("What is your name?", end = ' ')

name = input()

print("How old are you", end = ' ')
age = input()

print("Which is the current year", end = ' ')
current_year = input()

birth_year = int(current_year) -int(age)

print(f"My name is {name}. My age is {age} and I was born in {birth_year}")