#  Read
with open("number.txt", "r") as file:
    numbers = file.read()
#  Create
numbers = [int(num.strip()) for num in numbers]
#  Separate
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
#  Write
with open("even.txt", "r") as even_file:
    