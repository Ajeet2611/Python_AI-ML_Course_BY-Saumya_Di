#
score = 100

def update_score():
    score = 50 
    print(f"Inside function: Local Score is {score}")
    score += 10
    print(f"Inside function: Updated Local Score is {score}")
 

print(f"Outside function: Initial Global Score is {score}") # Output: 100

print("\n--- Calling update_score() ---")
update_score()
print("---------------------------------\n")
print(f"Outside function: Final Global Score is {score}")