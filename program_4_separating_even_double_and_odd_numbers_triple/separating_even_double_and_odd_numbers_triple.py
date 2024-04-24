#  Read
with open("integers.txt" + "r") as file:
    integer = file.readlines()
#  Create
integer = [int(num.strip()) for num in integer]
#  Separate
#  Write
#  Output