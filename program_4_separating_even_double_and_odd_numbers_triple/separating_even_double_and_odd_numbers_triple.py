#  Read
with open("integers.txt" + "r") as file:
    integer = file.readlines()
#  Create
integer = [int(num.strip()) for num in integer]
#  Separate
square_even_numbers = [num ** 2 for num in integer if num == 0]
#  Write
#  Output