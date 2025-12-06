#Ask the user for their 3 favorite movies and store them in a list, then print the list and its length
print("\t\t\n\nWelcome to enter your favorite movies program!\n\n")

first_movie = input("Please enter your 1st favorite movie name: ")
second_movie = input("Please enter your 2nd favorite movie name : ")
third_movie = input("Please enter your 3rd favorite movie name : ")
favorite_movies = [first_movie, second_movie, third_movie]
print("Your favorite movies are:", favorite_movies)
print("Number of favorite movies you entered:", len(favorite_movies))

