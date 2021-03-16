# RecModel source code profiling

# `predict` and `rank`

In order to understand how to measure the `inference_time(ms)`

we check the `predict` and `rank` :

1. `naive_baseline_model.py`
2. `slim_model.py`
3. `recwalk_model.py`

| Model  | predict| rank| note|
|--------|--------|-----|-----|
| random | N/A| random sampling| 1. coverage 100% <br> 2. performance baseline|
| slim   | predict single user for random selected items partitioning topN | 1. accuracy/inference time can be tune by regularization parameter|
| rec_walk | N/A| k steps, inner product of (starting vector, transistion matrix) and partitioning top k |accuracy inference time can be tune by step k|

`rank` method : 

items : np.ndarray shape (N, ) random selected items

users : np.ndarray shape(N, ) recommend respect to user_i

topN : int chopped at topN

# Need Implementation

`eval_topn` and `compute_hit`

1. [ ] exclude items which user already boughted from the radomling for predcition in `base_model.py` line 73

2. [x] generate random samples without replacement line 64 in `base_model.py`

3. [ ] radom sampling the user instead of all the users in `eval_topn` function and check how DRecPy do the same things.

   1. [x] DRecPy strategy and assert statement(they do random samling)
   2. [ ] Do random sampling and assert statement 
