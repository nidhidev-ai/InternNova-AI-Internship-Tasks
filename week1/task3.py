# Predict Pass/Fail

name = input("Enter your name: ")
marks = float(input("Enter your marks: "))

if marks >= 35:
    print(name, "has Passed.")
else:
    print(name, "has Failed.")

# Celsius to Fahrenheit Converter

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit) 

# Age Eligibility Checker

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to Vote.")
else:
    print("Not Eligible to Vote.")

# Attendance Percentage Checker    

classes_attended = int(input("Enter classes attended: "))
total_classes = int(input("Enter total classes: "))

attendance = (classes_attended / total_classes) * 100

print("Attendance Percentage:", attendance)

if attendance >= 75:
    print("Eligible for Exam.")
else:
    print("Not Eligible for Exam.")