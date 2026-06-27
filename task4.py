movies = {
    "Action": ["Avengers", "Batman", "Mission Impossible"],
    "Comedy": ["The Mask", "Jumanji", "Home Alone"],
    "Horror": ["The Conjuring", "Insidious", "Annabelle"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"]
}

genre = input("Enter your favorite genre: ")

if genre in movies:
    print("Recommended Movies:")
    for movie in movies[genre]:
        print(movie)
else:
    print("Genre not found")


movies = {
    "Action": ["Avengers", "Batman", "Mission Impossible"],
    "Comedy": ["The Mask", "Jumanji", "Home Alone"],
    "Horror": ["The Conjuring", "Insidious", "Annabelle"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"]
}

genre = input("Enter your favorite genre: ")

if genre in movies:
    print("\nRecommended Movies:")
    
    for movie in movies[genre]:
        print(movie)
else:
    print("Genre not found")


    movies = {
    "Action": ["Avengers", "Batman", "Mission Impossible"],
    "Comedy": ["The Mask", "Jumanji", "Home Alone"],
    "Horror": ["The Conjuring", "Insidious", "Annabelle"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"]
}

genre = input("Enter your favorite genre: ")

if genre in movies:
    print("\nRecommended Movies:")
    
    for movie in movies[genre]:
        print(movie)
else:
    print("Genre not found")