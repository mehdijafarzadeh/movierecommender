"""
Contains various recommondation implementations
all algorithms return a list of movieids
"""
import pandas as pd
import numpy as np
from movierecommender.utils import movies, ratings, model


def recommend_random(liked_items, k=5):
    """
    return k random unseen movies for user
    """
    # filter out movies that are in the list of liked movies
    row_filter = ~movies.index.isin(liked_items)
    # return movie ids
    return movies.loc[row_filter].sample(k).index


def recommend_nmf(queries, rating, k=5):

    rating = [int(rating) for rating in rating]
    # Create a zip object from two lists
    zipbObj = zip(queries, rating)
    # Create a dictionary from zip object
    liked_items = dict(zipbObj)
    df = ratings.merge(movies, on='movieId')
    R = df.pivot_table(values='rating', index='userId', columns='title')
    R.fillna(0, inplace=True)
    Q = model.components_
    movielist = list(R.columns)
    emptylist = [0] * len(movielist)
    moviedict = dict(zip(movielist, emptylist))
    for movie, rating in liked_items.items():
        moviedict[movie] = rating
    movie_df = pd.DataFrame(list(moviedict.values()), index=moviedict.keys())
    movie_df = movie_df.transpose()
    P = model.transform(movie_df)
    predictions = np.dot(P, Q)
    recommendations = pd.DataFrame(predictions, columns=movie_df.columns)
    end_recomms = recommendations[(movie_df == 0)].T
    end_recomms.columns = ['predicted_rating']
    return end_recomms['predicted_rating'].sort_values(ascending=False)[
        :k].index


def recommend_cosine(liked_items, ratings, k=5):
    pass


def recommend_most_popular(liked_items, movie_item_avg, k=5):
    """
    return k most popular unseen movies for user
    """
    return None


if __name__ == '__main__':
    print(recommend_random([1, 2, 3]))
