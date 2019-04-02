the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears', 'apricots']
change = [1,'pennies',2,'dimes',3, 'quarters']

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"fruit of type {fruit}")


# We can go through mixed lists too

for i in change:
    print(f"Adding {i} to the list")

# we can build the list

elements = []

for i in range(0,6):
    print(f"Adding {i} to the list")
    # Append is a function that lists understand
    elements.append(i)

# We can print them out too

for i in elements:
    print(f"Element was {i}")

for a in range(0,10):
    print(f"What is the number {a}")