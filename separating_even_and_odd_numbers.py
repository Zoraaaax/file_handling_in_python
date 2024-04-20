#  Read
with open("numbers.txt", "r") as file:
    numbers = file.read().strip()
#  Create
numbers = [int(num) for num in numbers]
#  Separate
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
#  Write
with open("even.txt", "w") as even_file:
    for num in even_numbers:
        even_file.write(str(num) + '\n')

with open("odd.txt", "w") as odd_file:
    for num in odd_numbers:
        odd_file.write(str(num) + '\n')
