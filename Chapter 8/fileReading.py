# #with keyword
# with open ("report.txt","r") as f:
#     data = f.read()
#     print("File data :",data)

#read line by line
# with open ("newTextfile.txt") as f :
#     line1 = f.readline()
#     line2 = f.readline()
#     line3 = f.readline()
#     line4 = f.readline()
#     print("line 1",line1)
#     print("line 2",line2)
#     print("line 3",line3)
#     print("line 4",line4)

#read all lines

with open("newTextfile.txt") as f:
    lines = f.readlines()
    print(lines)