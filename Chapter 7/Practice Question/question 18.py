#Create a Programe using global keyword to modify a variable from inside a function
score = 100
def modify_global_score(points_to_add):
    global score 
    
    print(f"Inside function: Reading Global Score (before modification) is {score}")
    score += points_to_add
    print(f"Inside function: Updated Global Score is {score}")
    # --- Function Calls and Output ---

print(f"Outside function: Initial Global Score is {score}\n") # Output: 100

print("--- Calling modify_global_score(25) ---")
modify_global_score(25)
print("---------------------------------------\n")
print(f"Outside function: Final Global Score is {score}") # Output: 125