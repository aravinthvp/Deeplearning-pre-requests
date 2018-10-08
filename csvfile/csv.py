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


