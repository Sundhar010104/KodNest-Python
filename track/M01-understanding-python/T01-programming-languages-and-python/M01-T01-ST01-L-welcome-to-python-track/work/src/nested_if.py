# Read marks, attendance and project completion status
marks = int(input())
attnd = int(input())
prj = input()

# Check the academic requirements using compound condition
if marks >= 60 and attnd >= 75:
    # Check the project completion status using nested condition
    if prj == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")