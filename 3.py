#coding=utf-8
import numpy as np

# array = np.array([[1,2,3],
#                  [2,3,4]])
#
# print(array)
# print("number of dim",array.ndim) #�����ά��
# print("shape",array.shape) #�����shape��״
# print("size",array.size) #�����Ԫ�ظ���

# a = np.array([[2,3,4],
#               [3,4,5]])
# print(a)

# a = np.zeros((3,4)) #ȫ��0
# b = np.ones((3,4)) #ȫ��1
# c = np.empty((3,4)) #�ӽ�0�ľ���
# d = np.arange(10,20,2)#����range  ����
# e = np.arange(12,20,2).reshape((2,2))
# f = np.linspace(1,10,5)#���һ������
# print(f)


#-------------------------------����-------------------------------


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
# h = f*g #�����˷�
# j = np.dot(f,g)#����˷�
# k = np.dot(g,f)
# l = f.dot(g)
# print(h)
# print(j)
# print(k)
# print(l)


# a = np.random.random((2,4))#����0-1���������
# print(a)
# print(np.sum(a,axis=0))#��
# print(np.sum(a,axis=1))#��
# print(np.min(a))#������һ��
# print(np.max(a))#���ֵ��axis����ά��



#----------------------����2----------------------------
# 
# A = np.arange(2,14).reshape((3,4))
#
#
# print(np.mean(A))#ƽ��ֵ
# print(A.mean()) #ͬ��
# print(np.average(A)) #ͬ��
# print(np.argmax(A))#���ֵ��������СֵҲһ��
# print(np.median(A))#��λ��
# print(np.cumsum(A))#�����
# print(np.diff(A)) #����֮��Ĳ�
# print(np.nonzero(A))#��������Ԫ�ص�λ�ã�ǰ�к���
# print(np.sort(A)) #���е�����
# print(np.transpose(A))#�����ת��
# print(np.clip(A,5,9)) #С��3�ı��3������9�ı��9
# print(np.clip(A,9,5))
