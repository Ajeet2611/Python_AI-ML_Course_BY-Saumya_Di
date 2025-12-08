#write a program that prints the sum of first n natural numbers
#For example, if n = 5,then output should be 15 (1+2+3+4+5)
#(Hint:Keep a running total inside the loop.)
n = int(input("Enter a  number: "))# n = number upto which sum is to be calculated
sum = 0
i = 1
while i<=n :
    sum = i+sum


    i+=1
    
print("The sum of first",n,"natural numbers is :",sum)    