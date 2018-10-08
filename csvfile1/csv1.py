>>> import pandas as pd
>>> import os
>>> os.chdir('/home/aravind/Desktop')
>>> files = pd.read_csv("A.csv")
>>> files
    "Month","International airline passengers: monthly totals in thousands. Jan 49 ? Dec 60" 
0                                       "1949-01",112                                        
1                                       "1949-02",118                                        
2                                       "1949-03",132                                        
3                                       "1949-04",129                                        
4                                       "1949-05",121                                        
5                                       "1949-06",135                                        
6                                       "1949-07",148                                        
7                                       "1949-08",148                                        
8                                       "1949-09",136                                        
9                                       "1949-10",119                                        
10                                      "1949-11",104                                        
11                                      "1949-12",118                                        
12                                      "1950-01",115                                        
13                                      "1950-02",126                                        
14                                      "1950-03",141                                        
15                                      "1950-04",135                                        
16                                      "1950-05",125                                        
17                                      "1950-06",149                                        
18                                      "1950-07",170                                        
19                                      "1950-08",170                                        
20                                      "1950-09",158                                        
21                                      "1950-10",133                                        
22                                      "1950-11",114                                        
23                                      "1950-12",140                                        
24                                      "1951-01",145                                        
25                                      "1951-02",150                                        
26                                      "1951-03",178                                        
27                                      "1951-04",163                                        
28                                      "1951-05",172                                        
29                                      "1951-06",178                                        
..                                                 ...                                       
115                                     "1958-08",505                                        
116                                     "1958-09",404                                        
117                                     "1958-10",359                                        
118                                     "1958-11",310                                        
119                                     "1958-12",337                                        
120                                     "1959-01",360                                        
121                                     "1959-02",342                                        
122                                     "1959-03",406                                        
123                                     "1959-04",396                                        
124                                     "1959-05",420                                        
125                                     "1959-06",472                                        
126                                     "1959-07",548                                        
127                                     "1959-08",559                                        
128                                     "1959-09",463                                        
129                                     "1959-10",407                                        
130                                     "1959-11",362                                        
131                                     "1959-12",405                                        
132                                     "1960-01",417                                        
133                                     "1960-02",391                                        
134                                     "1960-03",419                                        
135                                     "1960-04",461                                        
136                                     "1960-05",472                                        
137                                     "1960-06",535                                        
138                                     "1960-07",622                                        
139                                     "1960-08",606                                        
140                                     "1960-09",508                                        
141                                     "1960-10",461                                        
142                                     "1960-11",390                                        
143                                     "1960-12",432                                        
144  International airline passengers: monthly tota...                                       

[145 rows x 1 columns]
>>> datetime.strptime("1960-12","%Y-%m")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'datetime' is not defined
>>> datetime.strptime("1960-12","%Y-%m")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'datetime' is not defined
>>> from datetime import datetime
>>> datetime.strptime("1960-12","%Y-%m")
datetime.datetime(1960, 12, 1, 0, 0)
