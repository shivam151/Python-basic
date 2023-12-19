salary= int(input("Enter your salary: "))

if not 10000 < salary < 50000:
    raise Exception("You are not eligible for this course")#This is called the coustom in the python.
else:
    print("You are eligible for this course")
