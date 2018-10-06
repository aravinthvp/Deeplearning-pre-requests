aravind@aravind-Inspiron-N4050:~$ python3
Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> a=np.array([1,2])]
  File "<stdin>", line 1
    a=np.array([1,2])]
                     ^
SyntaxError: invalid syntax
>>> a=np.array([1,2])
>>> b=np.array([2,1])
>>> dot=0
>>> for e,f in zip(a,b):
...    print(e)
... 
1
2
>>> for e,f in zip(a,b):
...    print(e*f)
... 
2
2
>>> for e,f in zip(a,b):
...    print(e,f)
... 
1 2
2 1
>>> for e,f in zip(a,b):
...    print(e+f)
... 
3
3
>>> dot =0
>>> for e,f in zip(a,b):
...    print(dot +=e*f)
  File "<stdin>", line 2
    print(dot +=e*f)
               ^
SyntaxError: invalid syntax
>>>    print(dot += e*f)
  File "<stdin>", line 1
    print(dot += e*f)
    ^
IndentationError: unexpected indent
>>> for e,f in zip(a,b):
...    dot += e*f
... 
>>> 
>>> dot
4
>>> a*b
array([2, 2])
>>> np.sum(a*b)
4
>>> np.dot(a,b)
4
>>> a.dot(b)
4
>>> b.dot(a)
4
>>> (a*a).sum()
5
>>> a
array([1, 2])
>>> b
array([2, 1])
>>> a*a
array([1, 4])
>>> a*b
array([2, 2])
>>> np.sqrt(5)
2.2360679774997898
>>> a=np.sqrt((a*a).sum())
>>> a
2.2360679774997898
>>> a=np.linalg.norm(a)
>>> a
2.2360679774997898
>>> 
