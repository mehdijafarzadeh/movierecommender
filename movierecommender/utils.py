from fuzzywuzzy import process
import pandas as pd
import os

# __file__
# /home/malte/miniconda3/lib/python3.7/site-packages/movierecommender/utils.py

# package_dir
# /home/malte/miniconda3/lib/python3.7/site-packages/movierecommender/
package_dir = os.path.dirname(__file__)

# print(package_dir)

# put the movieId into the row index!
movies_path = package_dir + '/data/ml-latest-small/movies.csv'
movies = pd.read_csv(movies_path, index_col=0) 
movie_average_rating = None
ratings = None
movie_item_matrix = None



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

if __name__ == '__main__':
    results = lookup_movie('star wars', movies['title'])
    print(results)

