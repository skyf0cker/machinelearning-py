# 机器学习-李宏毅-day1-course2

## 主题：regression
### 举例：
- 股票预测
- 自动驾驶
- 推荐系统

### Regression
*宝可梦的cp值？？？*

1. Find Model:**function**
2. Goodness of function:loss function:input a function and output:**how bad it is**    
loss:L(f) = L(w,b)
3. Best function:Gradient Descent(只要可微分):**随机选取，然后看微分斜率，学习率learning data（在线性回归好用，因为极小值的存在）**

### overfitting and regularization  

- overfitting:复杂的模型在测试集的结果不好，在训练集的特别好
- regularization正规化：减小过拟合：L1，L2
