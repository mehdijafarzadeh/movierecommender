import pandas as pd
import numpy as np
import pickle
from fuzzywuzzy import process
import os

#put the movieId into the row index!
movies = pd.read_csv('./data/ml-latest-small/movies.csv', index_col=0) 
movie_average_rating = None
ratings = None
movie_item_matrix = None 
genres = pd.read_csv('./data/movies_genres.csv', index_col=0)

#movies and genres
movies_genres = pd.concat([movies, genres], axis=1)

genres = ['romance', 'sci-fi', 'animation', 'film-noir', 'musical', 
'adventure', 'thriller','horror', 'documentary', 'fantasy', 
'mystery', 'children', 'comedy','crime', 'western', 'imax', 
'war', 'drama', 'action']


#import ratings
ratings_long = pd.read_csv('./data/ml-latest-small/ratings.csv')

# transform ratings
ratings = pd.pivot_table(ratings_long, 
                        values='rating', 
                        index='userId', 
                        columns='movieId')

movie_average_rating = ratings.mean(axis=0)

def lookup_movie(search_query, titles):
    """
    given a search query, uses fuzzy string matching to search for similar 
    strings in a pandas series of movie titles
    returns a list of search results. Each result is a tuple that contains 
    the title, the matching score and the movieId.
    """
    matches = process.extractBests(search_query, titles)
    # [(title, score, movieId), ...]
    return matches

def watched_movies(userId):
    '''
    this function creates a user-item-matrix of the ratings_long table
    and returns a list of all watched movies by a user (userId)
    '''
    ratings = pd.pivot_table(ratings_long, values='rating', index='userId', columns='movieId')
    watched_movies = ratings.loc[userId].dropna().index
    return list(watched_movies)


def replace_movie_ids(user, titles):
    new_user = {
            'ratings':{}
    }
    new_user['genres']=user['genres']
    for key in user['ratings'].keys():
        movie_id = lookup_movie(key, titles)[0][2]
        new_user['ratings'][movie_id] = user['ratings'][key]
    return new_user
    

def create_new_user(user):
    new_user = replace_movie_ids(user, movies['title'])
    vector = np.repeat(0, 193610)
    for key,val in new_user['ratings'].items():
        vector[key] = int(val)
    return vector
    
def load_model(filepath):
    model = pickle.load(open(filepath, 'rb'))
    return model
def create_neighborhood(user_vector):
    model = load_model('./model/k_nn_cosine.sav')
    distances, neighbor_ids = model.kneighbors(user_vector, n_neighbors=20)
    return neighbor_ids

def create_genre_index_filter(user):
    df = pd.DataFrame(columns=movies_genres.columns)
    for genre in user['genres']:
        df = pd.concat([df, movies_genres[movies_genres[genre] ==1]])
    df.drop_duplicates(inplace=True)
    return df.index


def neighbor_recommender(user):
    user_with_ids = replace_movie_ids(user, movies['title'])
    user_vector = create_new_user(user)
    neighbor_ids = create_neighborhood([user_vector])
    neighborhood = ratings_long.set_index('userId').loc[neighbor_ids[0]]
    recommendations = neighborhood.groupby('movieId')['rating'].sum().sort_values(ascending=False)
    #remove already watched movies
    item_filter = (~recommendations.index.isin(list(user_with_ids['ratings'].keys())))
    genre_index = create_genre_index_filter(user)
    genre_filter = (recommendations.index.isin(genre_index))
    recommendations = recommendations.loc[item_filter&genre_filter]
    return list(movies.loc[recommendations.index]['title'].head(10))



if __name__ == '__main__':
    results = lookup_movie('star wars', movies['title'])
    print(results)