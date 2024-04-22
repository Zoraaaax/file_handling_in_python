#  Read data
with open("students_name.txt", "r") as file:
    students_data = file.readlines()
#  Initial Values
highest_gwa = float('inf')
top_student_name = ""
#  Finding the Highest GWA
for data in students_data:
    name, gwa = students_data.strip().split(",")
    gwa = gwa(float)
    if gwa <= highest_gwa:
#  Output
