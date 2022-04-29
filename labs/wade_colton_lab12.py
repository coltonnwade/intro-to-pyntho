# Colton Wade
# Assignment 12


# List of movies
movie_list = ["Fast and Furious", "Harry Potter", "Star Wars"]
# Creates movies.txt file
movies = open("movies.txt", "w")


for movie in movie_list:
    movies.write(movie + "\n")



# Closes the movie.txt file
movies.close()

