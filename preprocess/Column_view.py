# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:13:44 2019

@author: 81479

单列可视化文件

实现被选取的列的单列可视化
"""

import numpy as np
from sys import argv
import pandas as pd
import os
import matplotlib.pyplot as plt

def Read_data(Data_path): 
    original_data = np.loadtxt(Data_path,delimiter=',')
    return original_data

def Plot(Data_name,load_data,Col_num,Save_path):
    Row,Col = load_data.shape
    x_range = np.arange(1,Row+1,1)
    plt.figure()
    plt.plot(x_range,load_data[:,Col_num])
    plt.xlabel('sample',fontsize=14)#x轴名称
    plt.ylabel('feature',fontsize=14)#y轴名称
    plt.tick_params(labelsize=13) # 坐标轴字体大小
    plt.savefig(Save_path+'/'+Data_name+'_ColView'+'.png')
    #plt.show()
    
if __name__ == '__main__':
    
    Data_name = argv[1]
    Col_num = argv[2]
    Col_num = int(Col_num)
    
    file_address = os.path.abspath('.') #文件目录   E:\work\preprocess
    file_address_parent = os.path.abspath('..') #文件的上级目录   E:\work
    
    Data_path = file_address_parent+'/'+'save_data'+'/'+Data_name+'_data'+'.csv'  #数据文件地址
    Data_path = os.path.abspath(Data_path)
    Save_path = file_address_parent+'/'+'picture' #数据存储地址
    
    if not os.path.isdir(Save_path):     #os.path.isdir()   查询是否存在该目录
        os.makedirs(Save_path)
    
    load_data = Read_data(Data_path)
    Plot(Data_name,load_data,Col_num,Save_path)
    