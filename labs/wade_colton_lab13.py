# Lab 13
# Colton Wade

# Function that adds three new movies
def append_movies():

    # Opens Movie.txt File in Append Mode and Adds three new movies
    movies = open("movies.txt", "a")
    movies.write("Elf\n")
    movies.write("Grinch\n")
    movies.write("Christmas Vacation\n")
    movies.close()

# Ends Function
append_movies()
