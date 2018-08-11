# 机器学习-李宏毅-day2-course2

## where the error come from
- bais
- variance(方差)

>期望值：  
在概率论和统计学中，一个离散性随机变量的期望值（或数学期望、或均值，亦简称期望，物理学中称为期待值）是试验中每次可能的结果乘以其结果概率的总和。换句话说，期望值像是随机试验在同样的机会下重复多次，所有那些可能状态平均的结果，便基本上等同“期望值”所期望的数。需要注意的是，期望值并不一定等同于常识中的“期望”——“期望值”也许与每一个结果都不相等。（换句话说，期望值是该变量输出值的平均数。期望值并不一定包含于变量的输出值集合里。）


***复杂的model的方差较大***  
***简单的model的偏差较大***

![error](http://chuantu.biz/t6/355/1533951644x-1376440252.jpg 'error')  

---
- underfitting:if your model cannot even fit the training examples, then you have large bias

- overfitting:if you can fit the training data ,but large error on testing data,then you probably have large variance

![error](http://chuantu.biz/t6/355/1533951731x-1376440240.png 'error')

  ----
- if underfitting:add more features as input :redesign your model
- if overfitting: more data or Regularization
Regularization may hurt your bias

### what you should NOt do:

![](http://chuantu.biz/t6/355/1533951853x-1376440150.png)

### what you should do:

![](http://chuantu.biz/t6/355/1533952068x-1404755576.png)
