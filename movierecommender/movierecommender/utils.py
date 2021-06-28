from fuzzywuzzy import process
import pandas as pd

# put the movieId into the row index!
movies = pd.read_csv('./data/ml-latest-small/movies.csv', index_col=0) 
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

