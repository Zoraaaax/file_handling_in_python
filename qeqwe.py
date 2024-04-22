#  Initial Values
highest_gwa = float('inf')
name_student = ""

#  Read data
with open("students_name.txt", "r") as file:
    student_data = file.readlines()

for data in student_data:
    name, gwa = data.strip().split(",")
    gwa = float(gwa)
    #  Finding the Highest GWA
    if gwa <= highest_gwa:
        highest_gwa = gwa
        top_student_name = name

print("The student with the highest GWA is", top_student_name, "with a GPA of", highest_gwa)