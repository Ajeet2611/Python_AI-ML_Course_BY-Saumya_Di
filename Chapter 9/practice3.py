#Create class student that take 3 marks and has a method average to calculate average ().
class Student:
    # Constructor (__init__) use karna behtar hota hai data store karne ke liye
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    # Average calculate karne ka alag method
    def calculate_average(self):
        total = self.sub1 + self.sub2 + self.sub3
        average = total / 3
        print(f"--- Report for {self.name} ---")
        print("Total marks obtained:", total)
        print("Average marks:", round(average, 3))
        
        if average >= 90:
            print("Grade: A")
        elif average >= 75:
            print("Grade: B")
        elif average >= 60:
            print("Grade: C")
        else:
            print("Grade: D")
        print("\n")

# Objects create karna aur method call karna
student1 = Student("Ajeet", 95, 88, 92)
student1.calculate_average()

student2 = Student("Ramesh", 76, 85, 80)
student2.calculate_average()

student3 = Student("Suresh", 55, 60, 58)
student3.calculate_average()