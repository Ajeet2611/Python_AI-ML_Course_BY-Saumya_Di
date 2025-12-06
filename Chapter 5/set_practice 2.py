#you are given a list of programming languages:
#["Python", "Java", "C++", "JavaScript", "Ruby","python", "java"]
#convert it into a set and print how many unique language Ajeet knows



languagesList =["Python", "Java", "C++", "JavaScript", "Ruby","python", "java"]
print(type(languagesList))  #<class 'list'>
#how to convert list into set
unique_languagesSet = set(languagesList)
print(type(unique_languagesSet))  #<class 'set'>
print("Unique programming languages known by Ajeet are : ",unique_languagesSet)
print("Ajeet knows ",len(unique_languagesSet)," unique programming languages.")
