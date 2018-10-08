>>> import pandas as pd
>>> import os
>>> os.getcwd()
'/home/aravind'
>>> os.chdir('/home/aravind/Desktop')
>>> os.getcwd()
'/home/aravind/Desktop'
>>> files = pa.read_csv("TechCrunchcontinentalUSA.csv")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pa' is not defined
>>> files = pd.read_csv("TechCrunchcontinentalUSA.csv")
>>> files
               permalink      ...              round
0               lifelock      ...                  b
1               lifelock      ...                  a
2               lifelock      ...                  c
3            mycityfaces      ...               seed
4               flypaper      ...                  a
5           infusionsoft      ...                  a
6                  gauto      ...               seed
7         chosenlist-com      ...               seed
8         chosenlist-com      ...              angel
9                   digg      ...                  b
10                  digg      ...                  a
11              facebook      ...              angel
12              facebook      ...                  a
13              facebook      ...                  b
14              facebook      ...                  c
15              facebook      ...                  c
16              facebook      ...                  c
17              facebook      ...         debt_round
18           photobucket      ...                  b
19           photobucket      ...                  a
20             omnidrive      ...              angel
21                  geni      ...                  a
22                  geni      ...                  b
23               twitter      ...                  b
24               twitter      ...                  c
25           stumbleupon      ...               seed
26                gizmoz      ...                  a
27                gizmoz      ...                  b
28                scribd      ...               seed
29                scribd      ...              angel
...                  ...      ...                ...
1430            fyreball      ...              angel
1431      delve-networks      ...               seed
1432      delve-networks      ...                  a
1433           livemocha      ...                  a
1434  mercentcorporation      ...                  b
1435           cleverset      ...              angel
1436           cleverset      ...                  a
1437           cleverset      ...              angel
1438       liquidplanner      ...              angel
1439             limeade      ...              angel
1440               yodio      ...                  a
1441         tastemakers      ...                  a
1442      whitepages-com      ...                  a
1443      revenuescience      ...                  e
1444            gotvoice      ...                  a
1445   cardomain-network      ...                  a
1446               mpire      ...                  a
1447               mpire      ...                  b
1448         teachstreet      ...                  a
1449            estately      ...              angel
1450             infinia      ...                  b
1451             infinia      ...                  a
1452           m-metrics      ...                  b
1453                cozi      ...                  a
1454                cozi      ...                  c
1455             trusera      ...              angel
1456          alerts-com      ...                  a
1457               myrio      ...       unattributed
1458       grid-networks      ...                  a
1459       grid-networks      ...                  b

[1460 rows x 10 columns]
>>> files = pd.read_csv("TechCrunchcontinentalUSA.csv", header=None)
>>> type(files)
<class 'pandas.core.frame.DataFrame'>
>>> files.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1461 entries, 0 to 1460
Data columns (total 10 columns):
0    1461 non-null object
1    1461 non-null object
2    568 non-null object
3    1437 non-null object
4    1443 non-null object
5    1461 non-null object
6    1461 non-null object
7    1461 non-null object
8    1461 non-null object
9    1461 non-null object
dtypes: object(10)
memory usage: 114.2+ KB
>>> files.head(10)
                0               1  ...                 8      9
0       permalink         company  ...    raisedCurrency  round
1        lifelock        LifeLock  ...               USD      b
2        lifelock        LifeLock  ...               USD      a
3        lifelock        LifeLock  ...               USD      c
4     mycityfaces     MyCityFaces  ...               USD   seed
5        flypaper        Flypaper  ...               USD      a
6    infusionsoft    Infusionsoft  ...               USD      a
7           gauto           gAuto  ...               USD   seed
8  chosenlist-com  ChosenList.com  ...               USD   seed
9  chosenlist-com  ChosenList.com  ...               USD  angel

[10 rows x 10 columns]
>>> files.head(1)
           0        1        2  ...            7               8      9
0  permalink  company  numEmps  ...    raisedAmt  raisedCurrency  round

[1 rows x 10 columns]
>>> files[0,0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/aravind/.local/lib/python2.7/site-packages/pandas/core/frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "/home/aravind/.local/lib/python2.7/site-packages/pandas/core/frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "/home/aravind/.local/lib/python2.7/site-packages/pandas/core/generic.py", line 2489, in _get_item_cache
    values = self._data.get(item)
  File "/home/aravind/.local/lib/python2.7/site-packages/pandas/core/internals.py", line 4115, in get
    loc = self.items.get_loc(item)
  File "/home/aravind/.local/lib/python2.7/site-packages/pandas/core/indexes/base.py", line 3080, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 164, in pandas._libs.index.IndexEngine.get_loc
KeyError: (0, 0)
>>> files(0,0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'DataFrame' object is not callable
>>> M = files.as_matrix()
__main__:1: FutureWarning: Method .as_matrix will be removed in a future version. Use .values instead.
>>> type(M)
<type 'numpy.ndarray'>
>>> files[0]
0                permalink
1                 lifelock
2                 lifelock
3                 lifelock
4              mycityfaces
5                 flypaper
6             infusionsoft
7                    gauto
8           chosenlist-com
9           chosenlist-com
10                    digg
11                    digg
12                facebook
13                facebook
14                facebook
15                facebook
16                facebook
17                facebook
18                facebook
19             photobucket
20             photobucket
21               omnidrive
22                    geni
23                    geni
24                 twitter
25                 twitter
26             stumbleupon
27                  gizmoz
28                  gizmoz
29                  scribd
               ...        
1431              fyreball
1432        delve-networks
1433        delve-networks
1434             livemocha
1435    mercentcorporation
1436             cleverset
1437             cleverset
1438             cleverset
1439         liquidplanner
1440               limeade
1441                 yodio
1442           tastemakers
1443        whitepages-com
1444        revenuescience
1445              gotvoice
1446     cardomain-network
1447                 mpire
1448                 mpire
1449           teachstreet
1450              estately
1451               infinia
1452               infinia
1453             m-metrics
1454                  cozi
1455                  cozi
1456               trusera
1457            alerts-com
1458                 myrio
1459         grid-networks
1460         grid-networks
Name: 0, Length: 1461, dtype: object
>>> files.head()
             0            1        2  ...            7               8      9
0    permalink      company  numEmps  ...    raisedAmt  raisedCurrency  round
1     lifelock     LifeLock      NaN  ...      6850000             USD      b
2     lifelock     LifeLock      NaN  ...      6000000             USD      a
3     lifelock     LifeLock      NaN  ...     25000000             USD      c
4  mycityfaces  MyCityFaces        7  ...        50000             USD   seed

[5 rows x 10 columns]
>>> type(files[0])
<class 'pandas.core.series.Series'>
>>> files.iloc[0]
0         permalink
1           company
2           numEmps
3          category
4              city
5             state
6        fundedDate
7         raisedAmt
8    raisedCurrency
9             round
Name: 0, dtype: object
>>> files.ix[0]
0         permalink
1           company
2           numEmps
3          category
4              city
5             state
6        fundedDate
7         raisedAmt
8    raisedCurrency
9             round
Name: 0, dtype: object
>>> type(files,ix[0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ix' is not defined
>>> type(files.ix[0])
<class 'pandas.core.series.Series'>
>>> files[[0,2]]
                       0        2
0              permalink  numEmps
1               lifelock      NaN
2               lifelock      NaN
3               lifelock      NaN
4            mycityfaces        7
5               flypaper      NaN
6           infusionsoft      105
7                  gauto        4
8         chosenlist-com        5
9         chosenlist-com        5
10                  digg       60
11                  digg       60
12              facebook      450
13              facebook      450
14              facebook      450
15              facebook      450
16              facebook      450
17              facebook      450
18              facebook      450
19           photobucket       60
20           photobucket       60
21             omnidrive      NaN
22                  geni       18
23                  geni       18
24               twitter       17
25               twitter       17
26           stumbleupon      NaN
27                gizmoz      NaN
28                gizmoz      NaN
29                scribd       14
...                  ...      ...
1431            fyreball      NaN
1432      delve-networks      NaN
1433      delve-networks      NaN
1434           livemocha      NaN
1435  mercentcorporation       50
1436           cleverset      NaN
1437           cleverset      NaN
1438           cleverset      NaN
1439       liquidplanner       11
1440             limeade       10
1441               yodio        4
1442         tastemakers       11
1443      whitepages-com      125
1444      revenuescience      NaN
1445            gotvoice       15
1446   cardomain-network       50
1447               mpire      NaN
1448               mpire      NaN
1449         teachstreet        8
1450            estately      NaN
1451             infinia      NaN
1452             infinia      NaN
1453           m-metrics      NaN
1454                cozi       26
1455                cozi       26
1456             trusera       15
1457          alerts-com      NaN
1458               myrio       75
1459       grid-networks      NaN
1460       grid-networks      NaN

[1461 rows x 2 columns]
>>> files[files[0] < 5]
Empty DataFrame
Columns: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Index: []
>>> files [ files[0] < 5]
Empty DataFrame
Columns: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Index: []
>>> files[0] < 5
0       False
1       False
2       False
3       False
4       False
5       False
6       False
7       False
8       False
9       False
10      False
11      False
12      False
13      False
14      False
15      False
16      False
17      False
18      False
19      False
20      False
21      False
22      False
23      False
24      False
25      False
26      False
27      False
28      False
29      False
        ...  
1431    False
1432    False
1433    False
1434    False
1435    False
1436    False
1437    False
1438    False
1439    False
1440    False
1441    False
1442    False
1443    False
1444    False
1445    False
1446    False
1447    False
1448    False
1449    False
1450    False
1451    False
1452    False
1453    False
1454    False
1455    False
1456    False
1457    False
1458    False
1459    False
1460    False
Name: 0, Length: 1461, dtype: bool

