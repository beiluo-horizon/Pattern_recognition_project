# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:33:19 2019

@author: 81479
"""

import numpy as np
from sys import argv
import pandas as pd
import os
import json

def Find_data(Data_path): 
    original_data = np.loadtxt(Data_path)
    return original_data

def Find_label(Label_FC_path):
    original_label = np.loadtxt(Label_FC_path)
    return original_label

def Get_shape(dataMat):
    Row,Col = dataMat.shape
    return Row,Col

if __name__ == '__main__':
    
    Data_name = argv[1]
#    Data_name = 'TE'
    file_address = os.path.abspath('.') #文件目录   E:\work\preprocess
    file_address_parent = os.path.abspath('..') #文件的上级目录   E:\work

    Data_path = file_address_parent+'/'+'data'+'/'+Data_name+'/'+'dataMat'+'.txt'  #数据文件地址
    Label_FC_path = file_address_parent+'/'+'data'+'/'+Data_name+'/'+'label_clf'+'.txt' #数据标签地址
    
    Data_path = os.path.abspath(Data_path)
    Label_FC_path = os.path.abspath(Label_FC_path)
    
    Save_path = file_address_parent+'/'+'save_data' #数据存储地址
    Save_path_label = file_address_parent+'/'+'save_data' #标签存储地址
    
    if not os.path.isdir(Save_path):     #os.path.isdir()   查询是否存在该目录
        os.makedirs(Save_path)
        
    original_data = Find_data(Data_path)
    original_label = Find_label(Label_FC_path)
    data_row,data_col = Get_shape(original_data)
    data_shape = {
            '数据集行数':data_row, 
            '数据集列数':data_col,
            }
    
    jsonfilename = file_address_parent+'/information/'+Data_name+'_original_'+'_information'+'.json'
    with open (jsonfilename,'w') as obj:
        json.dump(data_shape,obj)
    np.savetxt(Save_path+'/'+Data_name+'_Selected_'+'data.csv', original_data, delimiter = ',')
    np.savetxt(Save_path_label+'/'+Data_name+'_Selected_'+'Label'+'.csv', original_label, delimiter = ',')
    
    