aravind@aravind-Inspiron-N4050:~$ python3
Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> m = np.array([[1,2],[2,3])
  File "<stdin>", line 1
    m = np.array([[1,2],[2,3])
                             ^
SyntaxError: invalid syntax
>>> m = np.array([[1,2],[2,3]])
>>> m
array([[1, 2],
       [2, 3]])
>>> mn = np.matrix([[1,2],[2,3]])
>>> mn
matrix([[1, 2],
        [2, 3]])
>>> l =[[1,2],[2,3]]
>>> l
[[1, 2], [2, 3]]
>>> l =np.list([[1,2],[2,3]])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'numpy' has no attribute 'list'
>>> l =np.dot([[1,2],[2,3]])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Required argument 'b' (pos 2) not found
>>> mn
matrix([[1, 2],
        [2, 3]])
>>> mn.T
matrix([[1, 2],
        [2, 3]])
>>> m.T
array([[1, 2],
       [2, 3]])
>>> a = m.T
>>> a
array([[1, 2],
       [2, 3]])
>>> a=np.array(mn)
>>> a
array([[1, 2],
       [2, 3]])
>>> a>t
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 't' is not defined
>>> a.T
array([[1, 2],
       [2, 3]])
>>> A = np.array(mn)
>>> A
array([[1, 2],
       [2, 3]])
>>> A.T
array([[1, 2],
       [2, 3]])