# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:04:00 2019

@author: 81479
"""

import numpy as np
from sklearn import preprocessing
from sys import argv
import pandas as pd
import os
import json

def MinMaxScaler(dataMat):
    std_process = preprocessing.MinMaxScaler().fit(dataMat)
    MinMax_data = std_process.transform(dataMat)
    return MinMax_data

def Get_data(Data_path): 
    original_data = np.loadtxt(Data_path,delimiter=',')
    return original_data
    
def Get_shape(dataMat):
    Row,Col = dataMat.shape
    return Row,Col
    
if __name__ == '__main__':
    
    Data_name = argv[1]
    file_address = os.path.abspath('.') #文件目录   E:\work\preprocess
    file_address_parent = os.path.abspath('..') #文件的上级目录   E:\work

    Data_path = file_address_parent+'/'+'save_data'+'/'+Data_name+'_Selected_'+'data'+'.csv'  #数据文件地址
    Label_FC_path = file_address_parent+'/'+'save_data'+'/'+Data_name+'_Selected_'+'Label'+'.csv' #数据标签地址
    
    Data_path = os.path.abspath(Data_path)
    Label_FC_path = os.path.abspath(Label_FC_path)
    
    Save_path = file_address_parent+'/'+'save_data' #数据存储地址
    Save_path_label = file_address_parent+'/'+'save_data' #标签存储地址
    
    if not os.path.isdir(Save_path):     #os.path.isdir()   查询是否存在该目录
        os.makedirs(Save_path)
        
    original_data = Get_data(Data_path)
    Scaler_data = MinMaxScaler(original_data)
    np.savetxt(Save_path+'/'+Data_name+'_MinMaxScaler_'+'data.csv', Scaler_data, delimiter = ',')

    data_row,data_col = Get_shape(Scaler_data)
    data_shape = {
            '数据集行数':data_row, 
            '数据集列数':data_col,
            }
    
    jsonfilename = file_address_parent+'/information/'+Data_name+'_MinMaxScaler_'+'information'+'.json'
    op_path =  file_address_parent+'/information/'+'op_'+'information'+'.json'
    with open (op_path,'r') as read_op:
        last_op = json.load(read_op)
        last_op['preprocess'] = 'MinMaxScaler'
    with open (op_path,'w') as write_op:
        json.dump(last_op,write_op)
    with open (jsonfilename,'w') as obj:
        json.dump(data_shape,obj)
    