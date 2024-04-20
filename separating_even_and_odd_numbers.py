#  Read
with open("number.txt", "r") as file:
    numbers = file.read()
#  Create
numbers = [int(num.strip()) for num in numbers]
#  Separate
#  Write