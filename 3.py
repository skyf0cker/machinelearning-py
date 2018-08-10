#coding=utf-8
import numpy as np

# array = np.array([[1,2,3],
#                  [2,3,4]])
#
# print(array)
# print("number of dim",array.ndim) #数组的维度
# print("shape",array.shape) #数组的shape形状
# print("size",array.size) #数组的元素个数

# a = np.array([[2,3,4],
#               [3,4,5]])
# print(a)

# a = np.zeros((3,4)) #全是0
# b = np.ones((3,4)) #全是1
# c = np.empty((3,4)) #接近0的矩阵
# d = np.arange(10,20,2)#类似range  步长
# e = np.arange(12,20,2).reshape((2,2))
# f = np.linspace(1,10,5)#最后一个步长
# print(f)


#-------------------------------运算-------------------------------


# a = np.array([10,20,30,40])
# b = np.arange(4)
#
# c= a-b
#
# d = a+b
# e = b**2
# print(e)

# f = np.array([[1,1],
#               [0,1]])
# g = np.arange(4).reshape((2,2))
#
# h = f*g #算术乘法
# j = np.dot(f,g)#矩阵乘法
# k = np.dot(g,f)
# l = f.dot(g)
# print(h)
# print(j)
# print(k)
# print(l)


# a = np.random.random((2,4))#生成0-1的随机矩阵
# print(a)
# print(np.sum(a,axis=0))#列
# print(np.sum(a,axis=1))#行
# print(np.min(a))#和上面一样
# print(np.max(a))#最大值，axis决定维度



#----------------------运算2----------------------------
# 
# A = np.arange(2,14).reshape((3,4))
#
#
# print(np.mean(A))#平均值
# print(A.mean()) #同上
# print(np.average(A)) #同上
# print(np.argmax(A))#最大值索引，最小值也一样
# print(np.median(A))#中位数
# print(np.cumsum(A))#逐步相加
# print(np.diff(A)) #两个之间的差
# print(np.nonzero(A))#输出非零的元素的位置，前行后列
# print(np.sort(A)) #逐行的排序
# print(np.transpose(A))#矩阵的转置
# print(np.clip(A,5,9)) #小于3的变成3，大于9的变成9
# print(np.clip(A,9,5))
