# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 09:30:42 2020

@author: GO
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
import matplotlib.mlab as mlab
from scipy.stats import norm


x = np.array([52,50,48,46.8,56,46,42.8,42.5,42,60,38,38,65,68,70,73])


mu =np.mean(x)
sigma =np.std(x)

num_bins = 6 #直方图柱子的数量 
n, bins, patches = plt.hist(x, num_bins,density=1, alpha=0.75) 
#直方图函数，x为x轴的值，normed=1表示为概率密度，即和为一，绿色方块，色深参数0.5.返回n个概率，直方块左边线的x值，及各个方块对象 
y = norm.pdf(bins, mu, sigma)#拟合一条最佳正态分布曲线y 
 
plt.grid(True)
plt.plot(bins, y, 'r--') #绘制y的曲线 
plt.xlabel('values') #绘制x轴 
plt.ylabel('Probability') #绘制y轴 
plt.title('Histogram : $\mu$=' + str(round(mu,2)) + ' $\sigma=$'+str(round(sigma,2)))  #中文标题 u'xxx' 
#plt.subplots_adjust(left=0.15)#左边距 
plt.show()






