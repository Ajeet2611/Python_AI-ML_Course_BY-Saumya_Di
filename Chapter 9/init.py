class student:
    schoolName = "ABC School"
    def __init__(self,name,course):
        self.name = name
        self.course = course
       
       
student1 = student("John", "Science")
print("School name is:", student1.schoolName)
print("Student name is:", student1.name)
print("Course enrolled:", student1.course)

student2 = student("Alice", "Mathematics")
print("School name is:", student2.schoolName)
print("Student name is:", student2.name)
print("Course enrolled:", student2.course)