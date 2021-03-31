'''
(py_37_ds) YuLong@MacBook-Pro:~/Desktop/Working_Area/recsys_im$ python get_netflix_movielens_millionsong/Movielens.py --dataset dataset/ml-20m/ratings.csv
'''
#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import scipy.sparse
from absl import app, flags
from absl.flags import FLAGS

flags.DEFINE_string(
    'dataset', 'ml-20m/ratings.csv', 'path to dataset')


def main(_argv):
    # Load the ratings data
    ratings = pd.read_csv(FLAGS.dataset)

    # Binarize the data as it will be used as implicit feedback data
    ratings = ratings.loc[ratings['rating'] >= 4, :].copy()
    ratings['rating'] = 1.0

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
    ML_20M = scipy.sparse.csr_matrix(
        (unique_users.shape[0], unique_movie.shape[0]), dtype=np.float32)

    # Put the actual values in the matrix
    ML_20M[ratings.loc[:, 'users'].values,
           ratings.loc[:, 'items'].values] = 1.0

    # Save the matrix.
    scipy.sparse.save_npz('ML_20M', ML_20M)


if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass
