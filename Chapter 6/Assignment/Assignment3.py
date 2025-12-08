#print all number between 1 to 50 except multiples of 5.

for i in range (1,51,1):
    if(i%5==0):
        continue
    print(i)

