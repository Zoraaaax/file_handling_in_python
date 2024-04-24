#  Write the file
with open("mylife.txt", "w") as file:

    #  While loop
    while True:
        line = input("Enter a line: ")
        file.writelines(line + "\n")
        more_lines = input("Are there more lines (y/n)? ")

#  Output