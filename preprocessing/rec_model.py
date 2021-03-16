'''
===================================================
processing data for rec_model repo input data
===================================================
EXPLANATION:
	REFERENCE 
        1. get_netflix_movielens_millionsong/Movielens.py
        2. RecModel_profling/getting_start.ipynb
        3. precoessing/tffm.py

    INPUTS DATA FORMAT
        (plain text)
        user_id, movie_id, rating, timestamp
        user_id, movie_id, rating, timestamp
        user_id, movie_id, rating, timestamp
        ...
    
    OUTPUT DATA FORMAT
        (sparse matrix)

                item_1, item_2, item_3, ... item_I
        
        user_1     0      0        1    ...   0
        user_2     0      0        0    ...   1
        ...
        user_U
INPUTS:
OPTIONAL INPUT:
OUTPUT:
EXAMPLE:
	(py_37_ds) YuLong@MacBook-Pro:~/Desktop/Working_Area/recsys_im$ python preprocessing/rec_model.py
      --data dataset/ml-100k/ua.base --processed_name ml_100k_trn
REVISION HISTORY:
	functionality1  date1 author1
	functionality2  date2 author2
'''
#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import scipy.sparse
from absl import app, flags
from absl.flags import FLAGS

flags.DEFINE_string(
    'data', 'ml-100k/ua.base', 'path to raw data')

flags.DEFINE_string(
    'processed_name', 'ml_100k_trn', 'name of processed training data')


def processing_ml_100k(_argv):
    ratings = {
        'userId':[],
        'movieId':[],
        'rating':[]
    }
    # Load the ratings data
    with open(FLAGS.data) as f:
        for line in f:
            (user_id, movie_id, rating, ts) = line.split('\t')
            # Binarize the data as it will be used as implicit feedback data
            if float(rating) >= 4.0:
                ratings['userId'].append(user_id)
                ratings['movieId'].append(movie_id)
                ratings['rating'].append(1.0)
    ratings = pd.DataFrame(ratings)
    
    # Create user to row mapping.
    unique_users = ratings['userId'].unique()
    user_mapping = {userid: ID for (userid, ID) in zip(
        unique_users, np.arange(len(unique_users)))}

    # Create movie to column mapping
    unique_movie = ratings['movieId'].unique()
    movie_mapping = {movieid: ID for (movieid, ID) in zip(
        unique_movie, np.arange(len(unique_movie)))}

    # Create new columns to index the matrix.
    ratings['items'] = [movie_mapping[movie] for movie in ratings['movieId']]
    ratings['users'] = [user_mapping[user] for user in ratings['userId']]

    # Construct the empty matrix
    user_item_interaction = scipy.sparse.csr_matrix(
        (unique_users.shape[0], unique_movie.shape[0]), dtype=np.float32)

    # Put the actual values in the matrix
    user_item_interaction[ratings.loc[:, 'users'].values,
           ratings.loc[:, 'items'].values] = 1.0

    # Save the matrix.
    scipy.sparse.save_npz(FLAGS.processed_name, user_item_interaction)


if __name__ == '__main__':
    try:
        app.run(processing_ml_100k)
    except SystemExit:
        pass
