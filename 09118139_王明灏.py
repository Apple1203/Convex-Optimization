'''
    water_filling algorithm in python
    @author:MHWang
    29/12/2019
'''
import numpy as np
import random
from matplotlib import pyplot as plt
def visualize_water(alpha, x, horizontal_line): # 可视化
    alpha = alpha.squeeze()
    x = x.squeeze()
    x_range = range(1, x.shape[0]+1)
    plt.xticks(x_range)
    plt.bar(x_range, alpha, color='#ff9966',
    width=1.0, edgecolor='#ff9966')
    plt.bar(x_range, x, bottom=alpha, color='#4db8ff', width=1.0)
    plt.axhline(y=horizontal_line,linewidth=1, color='k')
    plt.show()
def fill_water(alpha, total_water, precision):  # water_filling algorithm
    x_array = np.zeros((dimension,1),dtype='float_')
    left_water=total_water
    temp2=0.0
    for i in range (dimension):
        if(i!=dimension-1):     # 第一种情况，在遍历时还没有到达最后一组
            temp=alpha[i+1]-alpha[i]
            if(left_water/(i+1)<=temp):     # 水不够了
                temp2=left_water/(i+1)+alpha[i]    # find the horizontal line
                break
            else:
                left_water-=temp*(i+1)      # 水很充足
        else:       # 第二种情况，对最后一组的处理
            temp = 1 - alpha[i]
            if (left_water / (i + 1) <= temp):
                temp2 = left_water / (i + 1) + alpha[i]  # find the horizontal line
                break
            else:
                print('！！！！！题目生成错误，需要的水量小于1，一定能注满！！！！！')    # 异常处理
                temp2 = 1
    for i in range(dimension):      # 把各组注入的水量分别写入数组
        if(temp2 - alpha[i]>=0):
            x_array[i]=temp2-alpha[i]
        else:
            x_array[i]=0
    return x_array
alpha_range = [0.0, 1.0]
total_water = 1.0
dimension = 10
precision = 1e-6
alpha = np.random.uniform(low=alpha_range[0],high=alpha_range[1],size=(dimension, 1))
''' sort the ndarray  (major point)'''
alpha = np.sort(alpha,0)
print(alpha)
x = fill_water(alpha=alpha,total_water=total_water,precision=precision)
print(x)
print(x.sum())
horizontal_line = (alpha + x).min()
print(horizontal_line)
visualize_water(alpha, x, horizontal_line)