#Create a function login (username,password ="123") that print the credentials.
def login(username,password ="123"):
    print("credentials : ","\nusername : ",username,"\npassword : ",password)
print("--- Using Default Password ---")
login("ajeet123")
print("\n--- Passing a Custom Password ---")
login("ritesh456", "mysecretpin$123")