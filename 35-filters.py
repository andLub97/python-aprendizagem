our_movies=[("Interstellar", 10),("Ironman",8.2),("It follows",6.0),("X-men",3.0)]

# for movie in movies:
#     print(movie[1])

# for movie in movies:
#     if movie[1] >7:
#         print(movie)

def rating_filter(movies, max_rating):
    final_movies=[]
    for movie in movies:
        if movie[1]>= max_rating:
            final_movies.append(movie[0])
    return final_movies

print(rating_filter(our_movies, 5))