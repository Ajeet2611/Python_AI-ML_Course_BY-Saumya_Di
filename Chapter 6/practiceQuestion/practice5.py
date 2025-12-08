#Write a program to print this pattern using while loop
#*
#**
#***
#****


i = 1
while i<=4:
    j = 1
    while j<=i:
        print("*",end="")
        j = j+1
    print ()
    i = i+1

    #second methods

print ("second metods")

n = 1
while n<=4 :
    print("*" *n)

    n = n+1

print("we are out of while loop , and value of n should be 5 .")

