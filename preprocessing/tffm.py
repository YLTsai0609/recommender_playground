'''
===================================================
processing data for tffm repo input data
===================================================
EXPLANATION:
    REFERENCE 
        1. tensor-fm/movielens.py
        3. tffm_profiling/movielens_tffm.ipynb

    INPUTS DATA FORMAT
        (plain text)
        user_id, movie_id, rating, timestamp
        user_id, movie_id, rating, timestamp
        user_id, movie_id, rating, timestamp
        ...
    OUTPUT DATA FORMAT

    train_data : list user_id, item_id pair
    [
        {'user_id': '1', 'movie_id': '1'},
        {'user_id': '1', 'movie_id': '2'},
        {'user_id': '1', 'movie_id': '3'},
        {'user_id': '1', 'movie_id': '4'},
        {'user_id': '1', 'movie_id': '5'}
    ]

    y_train : np.ndarray, item rating

    train_users : set user_id
    train_items : set item_id

INPUTS:	
OPTIONAL INPUT:
OUTPUT:
EXAMPLE:
REVISION HISTORY:
'''
from sklearn.feature_extraction import DictVectorizer
import numpy as np



def load_movielens(filename, path="dataset/ml-100k/"):
    data = []
    y = []
    users = set()
    items = set()
    with open(path + filename) as f:
        for line in f:
            (user, movieid, rating, ts) = line.split('\t')
            data.append({"user_id": str(user), "movie_id": str(movieid)})
            y.append(float(rating))
            users.add(user)
            items.add(movieid)

    return (data, np.array(y), users, items)


if __name__ == "__main__":
    train_data, y_train, train_users, train_items = load_movielens("ua.base")
    test_data, y_test, test_users, test_items = load_movielens("ua.test")
    v = DictVectorizer()

    X_train = v.fit_transform(train_data) # sparse matrix user item interaction
    X_test = v.transform(test_data) # # sparse matrix user item interaction

    y_train.shape += (1,)

    # print(train_data.shape)
    print(y_train[:5], type(y_train))
    # print(list(train_users)[:5])
    # print(train_data, type(train_data))
