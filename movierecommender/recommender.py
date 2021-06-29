"""
Contains various recommondation implementations
all algorithms return a list of movieids
"""


from movierecommender.utils import movies


def recommend_random(liked_items, k=5):
    """
    return k random unseen movies for user 
    """
    # filter out movies that are in the list of liked movies
    row_filter = ~movies.index.isin(liked_items)
    # return movie ids
    return movies.loc[row_filter].sample(k).index


def recommend_nmf(liked_items, ratings, k=5):
    pass


def recommend_cosine(liked_items, ratings, k=5):
    pass

def recommend_most_popular(liked_items, movie_item_avg, k=5):
    """
    return k most popular unseen movies for user
    """
    return None




if __name__ == '__main__':
    print(recommend_random([1, 2, 3]))




