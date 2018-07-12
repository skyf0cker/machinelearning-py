import os 
import pandas as pd 
import requests

# r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

# with open('iris.data','w') as f:
# 	f.write(r.text)

# print("数据获取成功")

df = pd.read_csv('iris.data',names=["sepal length","sepal width","petal length","petal width","class"])

print(df.head())
#    sepal length  sepal width     ...       petal width        class
# 0           5.1          3.5     ...               0.2  Iris-setosa
# 1           4.9          3.0     ...               0.2  Iris-setosa
# 2           4.7          3.2     ...               0.2  Iris-setosa
# 3           4.6          3.1     ...               0.2  Iris-setosa
# 4           5.0          3.6     ...               0.2  Iris-setosa
print(df["sepal width"])    #通过列名索引数据
# 0      3.5
# 1      3.0
# 2      3.2
# 3      3.1
# 4      3.6
# 5      3.9
# 6      3.4
# 7      3.4
# 8      2.9
# 9      3.1
# 10     3.7
# 11     3.4
# 12     3.0
# 13     3.0
# 14     4.0
# 15     4.4
# 16     3.9
# 17     3.5
# 18     3.8
# 19     3.8
# 20     3.4
# 21     3.7
# 22     3.6
# 23     3.3
# 24     3.4
# 25     3.0
# 26     3.4
# 27     3.5
# 28     3.4
# 29     3.2
#       ... 
# 120    3.2
# 121    2.8
# 122    2.8
# 123    2.7
# 124    3.3
# 125    3.2
# 126    2.8
# 127    3.0
# 128    2.8
# 129    3.0
# 130    2.8
# 131    3.8
# 132    2.8
# 133    2.8
# 134    2.6
# 135    3.0
# 136    3.4
# 137    3.1
# 138    3.0
# 139    3.1
# 140    3.1
# 141    3.1
# 142    2.7
# 143    3.2
# 144    3.3
# 145    3.0
# 146    2.5
# 147    3.0
# 148    3.4
# 149    3.0
# Name: sepal width, Length: 150, dtype: float64
print(df.ix[:3,:2])         #df.ix[row,column]  通过切片索引
#    sepal length  sepal width
# 0           5.1          3.5
# 1           4.9          3.0
# 2           4.7          3.2
# 3           4.6          3.1
print(df.ix[:3,[x for x in df.columns if "width" in x]])
#    sepal width  petal width
# 0          3.5          0.2
# 1          3.0          0.2
# 2          3.2          0.2
# 3          3.1          0.2
print([x for x in df.columns if "width" in x])
#['sepal width', 'petal width']
print(df["class"].unique())  #列出符合他特定条件的所有内容
#['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']
print(df[df["class"] == "Iris-virginica"])
#      sepal length  sepal width       ...        petal width           class
# 100           6.3          3.3       ...                2.5  Iris-virginica
# 101           5.8          2.7       ...                1.9  Iris-virginica
# 102           7.1          3.0       ...                2.1  Iris-virginica
# 103           6.3          2.9       ...                1.8  Iris-virginica
# 104           6.5          3.0       ...                2.2  Iris-virginica
# 105           7.6          3.0       ...                2.1  Iris-virginica
# 106           4.9          2.5       ...                1.7  Iris-virginica
# 107           7.3          2.9       ...                1.8  Iris-virginica
# 108           6.7          2.5       ...                1.8  Iris-virginica
# 109           7.2          3.6       ...                2.5  Iris-virginica
# 110           6.5          3.2       ...                2.0  Iris-virginica
# 111           6.4          2.7       ...                1.9  Iris-virginica
# 112           6.8          3.0       ...                2.1  Iris-virginica
# 113           5.7          2.5       ...                2.0  Iris-virginica
# 114           5.8          2.8       ...                2.4  Iris-virginica
# 115           6.4          3.2       ...                2.3  Iris-virginica
# 116           6.5          3.0       ...                1.8  Iris-virginica
# 117           7.7          3.8       ...                2.2  Iris-virginica
# 118           7.7          2.6       ...                2.3  Iris-virginica
# 119           6.0          2.2       ...                1.5  Iris-virginica
# 120           6.9          3.2       ...                2.3  Iris-virginica
# 121           5.6          2.8       ...                2.0  Iris-virginica
# 122           7.7          2.8       ...                2.0  Iris-virginica
# 123           6.3          2.7       ...                1.8  Iris-virginica
# 124           6.7          3.3       ...                2.1  Iris-virginica
# 125           7.2          3.2       ...                1.8  Iris-virginica
# 126           6.2          2.8       ...                1.8  Iris-virginica
# 127           6.1          3.0       ...                1.8  Iris-virginica
# 128           6.4          2.8       ...                2.1  Iris-virginica
# 129           7.2          3.0       ...                1.6  Iris-virginica
# 130           7.4          2.8       ...                1.9  Iris-virginica
# 131           7.9          3.8       ...                2.0  Iris-virginica
# 132           6.4          2.8       ...                2.2  Iris-virginica
# 133           6.3          2.8       ...                1.5  Iris-virginica
# 134           6.1          2.6       ...                1.4  Iris-virginica
# 135           7.7          3.0       ...                2.3  Iris-virginica
# 136           6.3          3.4       ...                2.4  Iris-virginica
# 137           6.4          3.1       ...                1.8  Iris-virginica
# 138           6.0          3.0       ...                1.8  Iris-virginica
# 139           6.9          3.1       ...                2.1  Iris-virginica
# 140           6.7          3.1       ...                2.4  Iris-virginica
# 141           6.9          3.1       ...                2.3  Iris-virginica
# 142           5.8          2.7       ...                1.9  Iris-virginica
# 143           6.8          3.2       ...                2.3  Iris-virginica
# 144           6.7          3.3       ...                2.5  Iris-virginica
# 145           6.7          3.0       ...                2.3  Iris-virginica
# 146           6.3          2.5       ...                1.9  Iris-virginica
# 147           6.5          3.0       ...                2.0  Iris-virginica
# 148           6.2          3.4       ...                2.3  Iris-virginica
# 149           5.9          3.0       ...                1.8  Iris-virginica
# 
# 


virginica = df[df["class"] == "Iris-virginica"].reset_index(drop=True)
#重新set为一个dataframe，并重新排序
print(virginica)

#     sepal length  sepal width       ...        petal width           class
# 0            6.3          3.3       ...                2.5  Iris-virginica
# 1            5.8          2.7       ...                1.9  Iris-virginica
# 2            7.1          3.0       ...                2.1  Iris-virginica
# 3            6.3          2.9       ...                1.8  Iris-virginica
# 4            6.5          3.0       ...                2.2  Iris-virginica
# 5            7.6          3.0       ...                2.1  Iris-virginica
# 6            4.9          2.5       ...                1.7  Iris-virginica
# 7            7.3          2.9       ...                1.8  Iris-virginica
# 8            6.7          2.5       ...                1.8  Iris-virginica
# 9            7.2          3.6       ...                2.5  Iris-virginica
# 10           6.5          3.2       ...                2.0  Iris-virginica
# 11           6.4          2.7       ...                1.9  Iris-virginica
# 12           6.8          3.0       ...                2.1  Iris-virginica
# 13           5.7          2.5       ...                2.0  Iris-virginica
# 14           5.8          2.8       ...                2.4  Iris-virginica
# 15           6.4          3.2       ...                2.3  Iris-virginica
# 16           6.5          3.0       ...                1.8  Iris-virginica
# 17           7.7          3.8       ...                2.2  Iris-virginica
# 18           7.7          2.6       ...                2.3  Iris-virginica
# 19           6.0          2.2       ...                1.5  Iris-virginica
# 20           6.9          3.2       ...                2.3  Iris-virginica
# 21           5.6          2.8       ...                2.0  Iris-virginica
# 22           7.7          2.8       ...                2.0  Iris-virginica
# 23           6.3          2.7       ...                1.8  Iris-virginica
# 24           6.7          3.3       ...                2.1  Iris-virginica
# 25           7.2          3.2       ...                1.8  Iris-virginica
# 26           6.2          2.8       ...                1.8  Iris-virginica
# 27           6.1          3.0       ...                1.8  Iris-virginica
# 28           6.4          2.8       ...                2.1  Iris-virginica
# 29           7.2          3.0       ...                1.6  Iris-virginica
# 30           7.4          2.8       ...                1.9  Iris-virginica
# 31           7.9          3.8       ...                2.0  Iris-virginica
# 32           6.4          2.8       ...                2.2  Iris-virginica
# 33           6.3          2.8       ...                1.5  Iris-virginica
# 34           6.1          2.6       ...                1.4  Iris-virginica
# 35           7.7          3.0       ...                2.3  Iris-virginica
# 36           6.3          3.4       ...                2.4  Iris-virginica
# 37           6.4          3.1       ...                1.8  Iris-virginica
# 38           6.0          3.0       ...                1.8  Iris-virginica
# 39           6.9          3.1       ...                2.1  Iris-virginica
# 40           6.7          3.1       ...                2.4  Iris-virginica
# 41           6.9          3.1       ...                2.3  Iris-virginica
# 42           5.8          2.7       ...                1.9  Iris-virginica
# 43           6.8          3.2       ...                2.3  Iris-virginica
# 44           6.7          3.3       ...                2.5  Iris-virginica
# 45           6.7          3.0       ...                2.3  Iris-virginica
# 46           6.3          2.5       ...                1.9  Iris-virginica
# 47           6.5          3.0       ...                2.0  Iris-virginica
# 48           6.2          3.4       ...                2.3  Iris-virginica
# 49           5.9          3.0       ...                1.8  Iris-virginica