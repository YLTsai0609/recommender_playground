# Test?

No

# Compling fast_utils

``` 

(py_37_ds) YuLong@MacBook-Pro:~/Desktop/Working_Area/recsys_im/RecModel/RecModel/fast_utils$ python setup_models.py build_ext --inplace
```

``` 

Compiling sparse_tools.pyx because it changed.
Compiling ease_utils.pyx because it changed.
Compiling neighborhood_utils.pyx because it changed.
Compiling slim_utils.pyx because it changed.
[1/4] Cythonizing ease_utils.pyx
[2/4] Cythonizing neighborhood_utils.pyx
[3/4] Cythonizing slim_utils.pyx
/Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: ./slim_utils.pxd
  tree = Parsing.p_module(s, pxd, full_module_name)
[4/4] Cythonizing sparse_tools.pyx
running build_ext
building 'sparse_tools' extension
creating build
creating build/temp.macosx-10.9-x86_64-3.7
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/YuLong/miniconda3/envs/py_37_ds/include -arch x86_64 -I/Users/YuLong/miniconda3/envs/py_37_ds/include -arch x86_64 -I/Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include -I/Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include -I/Users/YuLong/miniconda3/envs/py_37_ds/include/python3.7m -c sparse_tools.c -o build/temp.macosx-10.9-x86_64-3.7/sparse_tools.o -fopenmp
```

looks like we need openmp or we invoke Apple-gcc.

[try with offical gcc instead of apple gcc](https://stackoverflow.com/questions/58344183/how-can-i-install-openmp-on-my-new-macbook-pro-with-mac-os-catalina)

Then we succeed!

log below:

``` 

building 'sparse_tools' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/YuLong/miniconda3/envs/py_37_ds/include -arch x86_64 -I/Users/YuLong/miniconda3/envs/py_37_ds/include -arch x86_64 -I/Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include -I/Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include -I/Users/YuLong/miniconda3/envs/py_37_ds/include/python3.7m -c sparse_tools.c -o build/temp.macosx-10.9-x86_64-3.7/sparse_tools.o -fopenmp
In file included from /Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1822,
                 from /Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:12,
                 from /Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from sparse_tools.c:635:
/Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:17:2: warning: #warning "Using deprecated NumPy API, disable it with " "#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
   17 | #warning "Using deprecated NumPy API, disable it with " \
      |  ^~~~~~~
gcc -bundle -undefined dynamic_lookup -L/Users/YuLong/miniconda3/envs/py_37_ds/lib -arch x86_64 -L/Users/YuLong/miniconda3/envs/py_37_ds/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.9-x86_64-3.7/sparse_tools.o -o /Users/YuLong/Desktop/Working_Area/recsys_im/RecModel/RecModel/fast_utils/sparse_tools.cpython-37m-darwin.so -fopenmp
building 'ease_utils' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/YuLong/miniconda3/envs/py_37_ds/include -arch x86_64 -I/Users/YuLong/miniconda3/envs/py_37_ds/include -arch x86_64 -I/Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include -I/Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include -I/Users/YuLong/miniconda3/envs/py_37_ds/include/python3.7m -c ease_utils.c -o build/temp.macosx-10.9-x86_64-3.7/ease_utils.o -fopenmp
In file included from /Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1822,
                 from /Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:12,
                 from /Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from ease_utils.c:635:
/Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:17:2: warning: #warning "Using deprecated NumPy API, disable it with " "#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
   17 | #warning "Using deprecated NumPy API, disable it with " \
      |  ^~~~~~~
gcc -bundle -undefined dynamic_lookup -L/Users/YuLong/miniconda3/envs/py_37_ds/lib -arch x86_64 -L/Users/YuLong/miniconda3/envs/py_37_ds/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.9-x86_64-3.7/ease_utils.o -o /Users/YuLong/Desktop/Working_Area/recsys_im/RecModel/RecModel/fast_utils/ease_utils.cpython-37m-darwin.so -fopenmp
building 'neighborhood_utils' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/YuLong/miniconda3/envs/py_37_ds/include -arch x86_64 -I/Users/YuLong/miniconda3/envs/py_37_ds/include -arch x86_64 -I/Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include -I/Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include -I/Users/YuLong/miniconda3/envs/py_37_ds/include/python3.7m -c neighborhood_utils.c -o build/temp.macosx-10.9-x86_64-3.7/neighborhood_utils.o -fopenmp
In file included from /Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1822,
                 from /Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:12,
                 from /Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from neighborhood_utils.c:635:
/Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:17:2: warning: #warning "Using deprecated NumPy API, disable it with " "#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
   17 | #warning "Using deprecated NumPy API, disable it with " \
      |  ^~~~~~~
gcc -bundle -undefined dynamic_lookup -L/Users/YuLong/miniconda3/envs/py_37_ds/lib -arch x86_64 -L/Users/YuLong/miniconda3/envs/py_37_ds/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.9-x86_64-3.7/neighborhood_utils.o -o /Users/YuLong/Desktop/Working_Area/recsys_im/RecModel/RecModel/fast_utils/neighborhood_utils.cpython-37m-darwin.so -fopenmp
building 'slim_utils' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/YuLong/miniconda3/envs/py_37_ds/include -arch x86_64 -I/Users/YuLong/miniconda3/envs/py_37_ds/include -arch x86_64 -I/Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include -I/Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include -I/Users/YuLong/miniconda3/envs/py_37_ds/include/python3.7m -c slim_utils.c -o build/temp.macosx-10.9-x86_64-3.7/slim_utils.o -fopenmp
In file included from /Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1822,
                 from /Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:12,
                 from /Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4,
                 from slim_utils.c:635:
/Users/YuLong/miniconda3/envs/py_37_ds/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:17:2: warning: #warning "Using deprecated NumPy API, disable it with " "#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-Wcpp]
   17 | #warning "Using deprecated NumPy API, disable it with " \
      |  ^~~~~~~
slim_utils.c: In function '__pyx_fuse_0__pyx_f_10slim_utils_train_Slim':
slim_utils.c:5078:35: warning: comparison of integer expressions of different signedness: 'int' and 'unsigned int' [-Wsign-compare]
 5078 |   for (__pyx_t_11 = 0; __pyx_t_11 < __pyx_t_6; __pyx_t_11+=1) {
      |                                   ^
slim_utils.c:5232:39: warning: comparison of integer expressions of different signedness: 'int' and 'unsigned int' [-Wsign-compare]
 5232 |       for (__pyx_t_13 = 0; __pyx_t_13 < __pyx_t_15; __pyx_t_13+=1) {
      |                                       ^
slim_utils.c:5265:39: warning: comparison of integer expressions of different signedness: 'int' and 'unsigned int' [-Wsign-compare]
 5265 |       for (__pyx_t_13 = 0; __pyx_t_13 < __pyx_t_15; __pyx_t_13+=1) {
      |                                       ^
slim_utils.c:5469:35: warning: comparison of integer expressions of different signedness: 'int' and 'unsigned int' [-Wsign-compare]
 5469 |   for (__pyx_t_11 = 0; __pyx_t_11 < __pyx_t_6; __pyx_t_11+=1) {
      |                                   ^
slim_utils.c:5528:35: warning: comparison of integer expressions of different signedness: 'int' and 'unsigned int' [-Wsign-compare]
 5528 |   for (__pyx_t_11 = 0; __pyx_t_11 < __pyx_t_6; __pyx_t_11+=1) {
      |                                   ^
slim_utils.c: In function '__pyx_fuse_1__pyx_f_10slim_utils_train_Slim':
slim_utils.c:6194:35: warning: comparison of integer expressions of different signedness: 'int' and 'unsigned int' [-Wsign-compare]
 6194 |   for (__pyx_t_11 = 0; __pyx_t_11 < __pyx_t_6; __pyx_t_11+=1) {
      |                                   ^
slim_utils.c:6348:39: warning: comparison of integer expressions of different signedness: 'int' and 'unsigned int' [-Wsign-compare]
 6348 |       for (__pyx_t_13 = 0; __pyx_t_13 < __pyx_t_15; __pyx_t_13+=1) {
      |                                       ^
slim_utils.c:6381:39: warning: comparison of integer expressions of different signedness: 'int' and 'unsigned int' [-Wsign-compare]
 6381 |       for (__pyx_t_13 = 0; __pyx_t_13 < __pyx_t_15; __pyx_t_13+=1) {
      |                                       ^
slim_utils.c:6585:35: warning: comparison of integer expressions of different signedness: 'int' and 'unsigned int' [-Wsign-compare]
 6585 |   for (__pyx_t_11 = 0; __pyx_t_11 < __pyx_t_6; __pyx_t_11+=1) {
      |                                   ^
slim_utils.c:6644:35: warning: comparison of integer expressions of different signedness: 'int' and 'unsigned int' [-Wsign-compare]
 6644 |   for (__pyx_t_11 = 0; __pyx_t_11 < __pyx_t_6; __pyx_t_11+=1) {
      |                                   ^
slim_utils.c: In function '__pyx_fuse_0__pyx_f_10slim_utils_sparse_co_descent_arr_intern':
slim_utils.c:7040:33: warning: comparison of integer expressions of different signedness: 'unsigned int' and 'int' [-Wsign-compare]
 7040 |   for (__pyx_t_9 = 0; __pyx_t_9 < __pyx_t_8; __pyx_t_9+=1) {
      |                                 ^
slim_utils.c:7509:35: warning: comparison of integer expressions of different signedness: 'unsigned int' and 'int' [-Wsign-compare]
 7509 |     __pyx_t_13 = ((__pyx_v_n_iter == (__pyx_v_max_iter - 1)) != 0);
      |                                   ^~
slim_utils.c: In function '__pyx_fuse_1__pyx_f_10slim_utils_sparse_co_descent_arr_intern':
slim_utils.c:7951:33: warning: comparison of integer expressions of different signedness: 'unsigned int' and 'int' [-Wsign-compare]
 7951 |   for (__pyx_t_9 = 0; __pyx_t_9 < __pyx_t_8; __pyx_t_9+=1) {
      |                                 ^
slim_utils.c:8420:35: warning: comparison of integer expressions of different signedness: 'unsigned int' and 'int' [-Wsign-compare]
 8420 |     __pyx_t_13 = ((__pyx_v_n_iter == (__pyx_v_max_iter - 1)) != 0);
      |                                   ^~
slim_utils.c: In function '__pyx_fuse_0__pyx_f_10slim_utils_sparse_co_descent_arr_par':
slim_utils.c:9120:41: warning: comparison of integer expressions of different signedness: 'int' and 'unsigned int' [-Wsign-compare]
 9120 |         for (__pyx_t_16 = 0; __pyx_t_16 < __pyx_t_19; __pyx_t_16+=1) {
      |                                         ^
slim_utils.c:9153:41: warning: comparison of integer expressions of different signedness: 'int' and 'unsigned int' [-Wsign-compare]
 9153 |         for (__pyx_t_16 = 0; __pyx_t_16 < __pyx_t_19; __pyx_t_16+=1) {
      |                                         ^
slim_utils.c: In function '__pyx_fuse_1__pyx_f_10slim_utils_sparse_co_descent_arr_par':
slim_utils.c:9659:41: warning: comparison of integer expressions of different signedness: 'int' and 'unsigned int' [-Wsign-compare]
 9659 |         for (__pyx_t_16 = 0; __pyx_t_16 < __pyx_t_19; __pyx_t_16+=1) {
      |                                         ^
slim_utils.c:9692:41: warning: comparison of integer expressions of different signedness: 'int' and 'unsigned int' [-Wsign-compare]
 9692 |         for (__pyx_t_16 = 0; __pyx_t_16 < __pyx_t_19; __pyx_t_16+=1) {
      |                                         ^
slim_utils.c: In function '__pyx_fuse_0__pyx_f_10slim_utils_sparse_co_descent_par':
slim_utils.c:10408:33: warning: comparison of integer expressions of different signedness: 'unsigned int' and 'int' [-Wsign-compare]
10408 |   for (__pyx_t_9 = 0; __pyx_t_9 < __pyx_t_8; __pyx_t_9+=1) {
      |                                 ^
slim_utils.c:10877:35: warning: comparison of integer expressions of different signedness: 'unsigned int' and 'int' [-Wsign-compare]
10877 |     __pyx_t_13 = ((__pyx_v_n_iter == (__pyx_v_max_iter - 1)) != 0);

```

we successfully get `.c` file and `.so` file from compile `pyx`

``` 

(py_37_ds) YuLong@MacBook-Pro:~/Desktop/Working_Area/recsys_im/RecModel/RecModel/fast_utils$ ls
__init__.pxd
__init__.py
__pycache__
build
ease_utils.c
ease_utils.cpython-37m-darwin.so
ease_utils.pyx
neighborhood_utils.c
neighborhood_utils.cpython-37m-darwin.so
neighborhood_utils.pyx
setup_models.py
slim_utils.c
slim_utils.cpython-37m-darwin.so
slim_utils.pxd
slim_utils.pyx
sparse_tools.c
sparse_tools.cpython-37m-darwin.so
sparse_tools.pxd
sparse_tools.pyx
```

requirements

 [ `sharedmem==0.3.8` ](https://pypi.org/project/sharedmem/0.3/)

# dlopen(mkl_rt.dll, 6): image not found

when running
 `naive_model_performance = naive_model.eval_topn(test_mat=test_data, topn = np.array([4, 10, 20, 50]), rand_sampled=1000)`

``` 

---------------------------------------------------------------------------
OSError                                   Traceback (most recent call last)
~/Desktop/Working_Area/recsys_im/RecModel/RecModel/base_model.py in _mkl(cls)
    190             try:
--> 191                 cls._mkl_rt = ctypes.CDLL('libmkl_rt.so')
    192             except OSError:

~/miniconda3/envs/py_37_ds/lib/python3.7/ctypes/__init__.py in __init__(self, name, mode, handle, use_errno, use_last_error)
    363         if handle is None:
--> 364             self._handle = _dlopen(self._name, mode)
    365         else:

OSError: dlopen(libmkl_rt.so, 6): image not found
```

it seems we need a `.so` file when running multithreading on `numpy`

[By this](https://gitter.im/eaton-lab/Lobby?at=59cedbd6cfeed2eb65694337)

it seems that my conda doesn't have the `.so` file.

we don't have `.so` but we have `dylib`

 `(base) YuLong@MacBook-Pro:~/Desktop/Working_Area/recsys_im$ find ~/miniconda3/ -name 'libmkl_rt*'`

``` 

/Users/YuLong/miniconda3//pkgs/mkl-2019.4-233/lib/libmkl_rt.dylib
/Users/YuLong/miniconda3//pkgs/mkl-2019.5-281/lib/libmkl_rt.dylib
/Users/YuLong/miniconda3//envs/py_37_ds/lib/libmkl_rt.dylib

```

we add `base_model.py` line 198

``` 

cls._mkl_rt = ctypes.CDLL('libmkl_rt.dylib') # yulong
```
