#  Read
with open("integers.txt" + "r") as file:
    numbers = file.readlines()
#  Create
numbers = [int(num.strip()) for num in numbers]
#  Separate
square_even_numbers = [num ** 2 for num in integer if num == 0]
#  Write
#  Output