from movierecommender.recommender import recommend_random


def test_recommend_random():
    items = [1, 2, 3]
    assert len(recommend_random(items)) == 5
