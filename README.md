# Recsys Playground

This repo could be serval usages : 

1. Playground of the research model about recommendation.
2. Building the analysis on the top of all of the models(e.g. data property and its suitable solution).
3. Building recommendation model zoo by adding utils and borrowing code from famous repo.
4. Imporving code of famous repo by creating branch.

# Getting Start

1. Set environment variable `RECSYS_IM_HOME` in your computer.

2. Start to surfing on the research code!

# Best Practice

1. Manage your dataset by soft-link
2. Put raw data to `dataset`, intermediate data to `project/data`
3. Always use tiny-piece of data(e.g. 100 samples) to make sure your code worked.
4. Use [`absl-py`](https://github.com/abseil/abseil-py) to make your argument parse easiler to read.
5. Use [`wandb`](https://github.com/wandb/client) to track your profiling / experiemtns. so that you can compare your result easily.

# Model Summary

Single line argument about all of the repos we cloned.

| Repo      | Description                                                           | Note |
|-----------|-----------------------------------------------------------------------|------|
| tffm      | developed in `tf1.8` , support any order interactions and sparse input | proflied by `tffm_profiling/` |
| tensor-fm | developed in `tf2.4` , wrapper by sklearn, easy to understand          | N/A  |
|pyFM |developed in python and cython, simple, portable code|N/A|
|RecModel |developed in cython, torch, SOTA on movielens, including `RecWalk` , `SLIM` |N/A|

# Bemchnark Summary

## Dataset

The property of dataset matters for the recoomendation system. Dataset Property Analysis(DPA) helps us to figure out what dataset the proposal of papers works.

The integrated dataset so far : 

| Dataset            | Date | Note |
|--------------------|------|------|
| MNIST              | 1/22 | N/A  |
| Movielens(ml-100k) | 1/22 | N/A  |
