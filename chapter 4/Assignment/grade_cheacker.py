#write a program to check grade based on marks(A/B/C/D) using if-elif-else statement
marks = int(input("Please enter your marks : " ))
if marks>=90 and marks<=100:
    print("Your grade is A")
elif marks>=75 and marks<90:
    print("your grade is B")
elif marks>=60 and marks<75:
    print("your grade is C")
elif marks>=40 and marks<60:
    print("your grade is D")
else:
    print("Your grade is Fail")
