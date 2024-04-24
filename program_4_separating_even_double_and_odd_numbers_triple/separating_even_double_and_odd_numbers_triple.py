#  Read
with open("integers.txt" + "r") as file:
    numbers = file.readlines()
#  Create
numbers = [int(num.strip()) for num in numbers]
#  Separate
square_even_numbers = [num ** 2 for num in numbers if num == 0]
cube_odd_numbers = [num ** 3 for num in numbers if num != 0]
#  Write
with open("double.txt", "w") as double_even_file:
    for num in square_even_numbers:
        double_even_file.write(str(num) + "\n")

with open("triple.txt", "w") as triple_odd_file:
    
#  Output