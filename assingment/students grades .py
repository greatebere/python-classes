""" problem statement
write a software to calculate  the semester grade points (GP) of student of lagos state university (LASU) IN faculty of science
ALL students of faculty are to offer the following 10 courses, each courses having their unit .

Course codde    unit
FOS101          3 units 
FOS102          4 units
FOS103          3 units
FOS104          4 units
FOS105          3 units
FOS106          4 uints
FOS107          3 units
FOS108          4 units
FOS109          3 units
FOS110          4 units

They are to provide the following Data
1. name
2. matric no
3.Departement
4.levels
5. course code
"""
# collecting data from students
print("welcome to the faculty of science this program that helps students calculate CPGA for each semester ")
student_names =input("Enter your name")
matric_no = int(input(f"Dear{students_name},kindly enter your matric no:"))
department =input("Enter your departemnt:")
levels = input("Enter your Department")
print(f"The following Data provided by {students_name} in {levels}1 with the matric no -{matric_no}  in the department of {department}")


def calculate_gp(score):
    if 70 <= score <= 100:
        return 5
    elif 60 <= score <= 69:
        return 4
    elif 50 <= score <= 59:
        return 3
    elif 45 <= score <= 49:
        return 2
    elif 40 <= score <= 44:
        return 1
    elif 0 <= score  <= 39:
        return 0
    else :
        return 0
    
    def calculate_semester_gpa(student_scores):
        courses = (
        "FOS101":3,
        "FOS102":4,
        "FOS103":3,
        "FOS104":4,
        "FOS105":3,
        "FOS106":4,
        "FOS107":3,
        "FOS108":4,
        "FOS109":3,
        "FOS110":4   
        )
# Initaiting
    total_units = 0
    total_weighted_gp = 0

    for course, score in students_scores. items():
        units = courses(course)
        gp = calculate_gp(scores)
        weighted_gp =  unit
        total_units += units
        total_weighted_gp += weighted_gp

     Gpa =total_weighted_gp /total_units
      return Gpa




# collecting students scores for each courses
student_scores =()
for course in ("FOS101","FOS102","FOS103","FOS104","FOS105","FOS106","FOS107","FOS108","FOS109","FOS110",)
    scores = int (input{"Enter scores for {}:"format{courses}})
    student_scores(courses) =scores
    
# calculating the Gpa
gpa = calculate_semester_gpa(student_scores)

# printing the results
print("\nstudents Name:", student_names)
print("matric No:",matric_no)
print("Department:", department)
print("level:",department)

print("semster GPA",round{gpa,2}) #rounding GPA to 2 decimals places

              







        )
        
