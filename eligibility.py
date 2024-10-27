print("NOTE : THIS EXAM IS ONLY FOR MATHS ,PHYSICS AND COMP STUDENTS")
name=str(input("Enter your name:"))
age=int(input("Enter your age:"))
if age<18 :
    print("You are not eligible for this exam")

elif age==18:
    print("You might wait for an year and then apply for the exam")

else:
    print("You are eligible for the exam")


gpa= float(input("Enter your cgpa:"))
if gpa>=3.0:
    print("You are eligible for the Exam")

else:
    print("You are not eligible for this exam")