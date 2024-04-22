#  Read data
with open("students_name.txt", "r") as file:
    students_data = file.readlines()
#  Initial Values
highest_gwa = float('inf')
top_student_name = ""
#  Finding the Highest GWA
for data in students_data:
    name, gwa = data.strip().split(",")
    gwa = float(gwa)
    if gwa <= highest_gwa:
        highest_gwa = gwa
        top_student_name = name
#  Output
print("The student with highest GWA is", top_student_name, "with a GWA of", highest_gwa)