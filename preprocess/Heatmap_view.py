# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:48:37 2019

@author: Tabgui


"""


import os
import numpy as np
import json
from sys import argv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#数据读取
def read_data(data_path):
    data = pd.read_csv(data_path,header = None)
    return data

#热力图绘制并保存
def find_corr(data,data_name,save_path):
    cor = data.corr()
    cor = abs(cor)
    fig= plt.figure(figsize = (30,30))
    
#   plt.figure(figsize=(12, 8))
    ax = fig
    cmap = sns.cubehelix_palette(start = 1.5, rot = 3, gamma=0.8, as_cmap = True)
    ax = sns.heatmap(cor,cmap=cmap,linewidths= 0.05,vmax = 1,vmin=0,annot = True,annot_kws={'size':8,'weight':'bold'},fmt='.1f')
    ax.set_title('Characteristic correlation')
    plt.savefig(save_path+'/'+data_name+'_Heatmap'+'.png')
    
if __name__ == '__main__':
    Data_name = argv[1]
    file_address = os.path.abspath('.') #文件目录   
    file_address_parent = os.path.abspath('..') #文件的上级目录  
    
    Data_path = file_address_parent+'/'+'save_data'+'/'+Data_name+'_data'+'.csv'  #数据文件地址
    Data_path = os.path.abspath(Data_path)
    Save_path = file_address_parent+'/'+'picture' #数据存储地址
    
    if not os.path.isdir(Save_path):     #os.path.isdir()   查询是否存在该目录
        os.makedirs(Save_path)
        
    data = read_data(Data_path)
    find_corr(data,Data_name,Save_path)