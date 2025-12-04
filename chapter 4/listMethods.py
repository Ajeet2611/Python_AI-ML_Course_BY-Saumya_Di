#Methods in list
print("-----list methods-----")

#indexing method
marks = [95, 85, 75, 65, 55]
marks[1] = 88
print("after changing marks list =", marks)

print("list of marks =", marks)

#append method

marks.append(45)
print("after appending marks list =", marks)

#insert method
marks.insert(2, 78)
print("after inserting marks list =", marks)
#remove method
marks.remove(65)

print("after removing marks list =", marks)
#pop method
popped_mark = marks.pop()
print("after popping marks list =", marks)
print("popped mark =", popped_mark)
#sort method
marks.sort()
print("after sorting marks list =", marks)
#reverse method
marks.reverse()
print("after reversing marks list =", marks)
#count method
count_85 = marks.count(85)
print("count of 85 in marks list =", count_85)
#clear method
marks.clear()
print("after clearing marks list =", marks)

#slicing method
marks = [95, 85, 75, 65, 55]
sliced_marks = marks[1:4]
print("sliced marks list (index 1 to 3) =", sliced_marks) 

#maximum and minimum method
max_mark = max(marks)
min_mark = min(marks)
print("maximum mark =", max_mark)
print("minimum mark =", min_mark)
#length method
length_of_marks = len(marks)
print("length of marks list =", length_of_marks)
