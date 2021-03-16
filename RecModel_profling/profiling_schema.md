# profling model

1. random(ok)
2. slim(ok)
3. RecWalk(ok)

# Benchmark

movielens - 20M (partial)

all of ML-20M, filtered by rating score >= 4 as implict feedback. we have : 

check SLIM table 1

users : 138287
items : 20720

small ML-20M

users : 20000
items : 5000

# metrics

1. training time unit (second) (ok)
2. inference time( mean of 50 times after warm start) unit (milisecond) (ok)
3. Recall@N(ok)
4. Coverage@N(ok)

where N = 5, 10, 20, 50

when evaluation recall and coverage, we random sample

n_users = 1000 in testing set

for each user, we random sample 1000 items to be ranked by model, then pick top N items(due to the performance issue)

we pick random_state = 2

## Table 1 / Figure 1

| Model | training time (s) | inference time(ms) | Recall@10 | Coverage@10 |
|-------|-------------------|--------------------|-----------|-------------|
| Random | N/A             |       N/A        |           |             |
| slim |              |               |           |             |
| RecWalk(steps=18) |              |               |           |             |

we pick random as a baseline model which can be reference the coverage.

slim model hyperparameter set :

alpha : 4.427181
l1_ratio : 0.31849
max_iter : 27
tolerance : 0.006841
cores : 8

recwalk model :

phi in code, alpha in paper : 0.005
steps : 18

## Table 2 / Figure 2

Line plot

x axis : topK, k = 5, 10, 20, 50

y1 axis : Recall

y2 axis : Coverage

color and marker : Model

## Table 3 / Figure 3

Knowing how the parameter "steps" and "phi" effect the perfermance Recall@10 and Coverage@10

x axis : steps (3, 6, 9, 12, 15, 18, 21)

y1 axis : Recall@10

y2 axis : Coverage@10

phi in code, alpha in paper : 1, 0.5, 0.1, 0.01, 0.005, 0.001

where alpha = 1 represent random walk

color : phi in code, alpha in paper 
