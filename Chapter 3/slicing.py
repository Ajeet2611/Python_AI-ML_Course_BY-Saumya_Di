#Understanding String Slicing in Python
str ="Python Programming"
# Slicing the string to get a substring
firstHalf = str[0:6]
secondHalf = str[7:18]
trialFirstHalf = str[:6]  # same as str[0:6]
trialSecondHalf = str[7:]  # same as str[7:18]
print("First Half:", firstHalf)  # Output: Python
print("Second Half:", secondHalf)  # Output: Programming
print("Trial First Half:", trialFirstHalf)  # Output: Python
print("Trial Second Half:", trialSecondHalf)  # Output: Programming
print("Full String using slicing:", str[:])  # Output: Python Programming
