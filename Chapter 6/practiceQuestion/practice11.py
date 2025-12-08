#Write a program that prints the multiplication table of any number entered the user using a for loop.

num = int (input("Please enter a number : "))

print("Printing a table ",num,"is :")

for i in range (1 , 11 ,1):
    print(num ,"x",i," = ",num*i)