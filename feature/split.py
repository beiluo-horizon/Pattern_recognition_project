# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 08:50:20 2019

@author: 81479
"""

import numpy as np
from sys import argv
import os
import json
import sklearn
from sklearn.model_selection import StratifiedKFold   #保证每折中样本比例相同
from sklearn.model_selection import KFold

def Split_data(x,y,para,Save_path,op):
    train_data,test_data,train_label,test_label = sklearn.model_selection.train_test_split(x,y,train_size=para,test_size=(1-para))
    np.savetxt(Save_path+'/'+op['Data_name']+'_'+op['preprocess']+'_Hold-out'+'_traindata.csv', train_data, delimiter = ',')
    np.savetxt(Save_path+'/'+op['Data_name']+'_'+op['preprocess']+'_Hold-out'+'_testdata.csv', test_data, delimiter = ',')
    np.savetxt(Save_path+'/'+op['Data_name']+'_'+op['preprocess']+'_Hold-out'+'_trainlabel.csv', train_label, delimiter = ',')
    np.savetxt(Save_path+'/'+op['Data_name']+'_'+op['preprocess']+'_Hold-out'+'_testlabel.csv', test_label, delimiter = ',')
    train_data_Row,train_data_Col = train_data.shape
    test_data_Row,test_data_Col = test_data.shape
    return train_data_Row,train_data_Col,test_data_Row,test_data_Col
    
def CV(x,y,para,Save_path,op):
    skf = StratifiedKFold(n_splits = para)
    i = 1
    for train_index,test_index in skf.split(x,y):
        train_data,test_data = x[train_index],x[test_index]
        train_label,test_label = y[train_index],y[test_index]
        np.savetxt(Save_path+'/'+op['Data_name']+'_'+op['preprocess']+'_CV'+'_traindata'+'_'+str(i)+'.csv', train_data, delimiter = ',')
        np.savetxt(Save_path+'/'+op['Data_name']+'_'+op['preprocess']+'_CV'+'_testdata'+'_'+str(i)+'.csv', test_data, delimiter = ',')
        np.savetxt(Save_path+'/'+op['Data_name']+'_'+op['preprocess']+'_CV'+'_trainlabel'+'_'+str(i)+'.csv', train_label, delimiter = ',')
        np.savetxt(Save_path+'/'+op['Data_name']+'_'+op['preprocess']+'_CV'+'_testlabel'+'_'+str(i)+'.csv', test_label, delimiter = ',')
        i +=1
    train_data_Row,train_data_Col = train_data.shape
    test_data_Row,test_data_Col = test_data.shape
    return train_data_Row,train_data_Col,test_data_Row,test_data_Col
if __name__ == '__main__':
    
    method = argv[1]
    parameter = argv[2]
    
    file_address = os.path.abspath('.') #文件目录   E:\work\feature
    file_address_parent = os.path.abspath('..') #文件的上级目录   E:\work
    
    op_path =  file_address_parent+'/information/'+'op_'+'information'+'.json'
    with open (op_path,'r') as read_op:
        last_op = json.load(read_op)
    
    Data_path = file_address_parent+'/'+'save_data'+'/'+last_op['Data_name']+'_'+last_op['preprocess']+'_data'+'.csv'  #数据文件地址
    Label_path = file_address_parent+'/'+'save_data'+'/'+last_op['Data_name']+'_Selected''_label'+'.csv'  #数据文件地址
    
    Save_path = file_address_parent+'/'+'save_data' #数据存储地址
    Save_path_label = file_address_parent+'/'+'save_data' #标签存储地址
    
    original_data = np.loadtxt(Data_path,delimiter=',')
    original_label = np.loadtxt(Label_path,delimiter=',')
    
    if method == 'Hold-out':     #使用留出法
        last_op['Hold_out_parameter'] = parameter
        parameter = float(parameter)
        train_data_Row,train_data_Col,test_data_Row,test_data_Col = Split_data(original_data,original_label,parameter,Save_path,last_op)
    else:               #否则使用交叉验证划分
        last_op['CV_parameter'] = parameter
        parameter = int(parameter)
        train_data_Row,train_data_Col,test_data_Row,test_data_Col = CV(original_data,original_label,parameter,Save_path,last_op)
        
    data_shape = {
        '训练集行数':train_data_Row, 
        '训练集列数':train_data_Col,
        '测试集行数':test_data_Row,
        '测试集列数':test_data_Col,
        }
    
    with open (op_path,'w') as write_op:
        last_op['split'] = method
        json.dump(last_op,write_op)
        
    jsonfilename = file_address_parent+'/information/'+last_op['Data_name']+'_'+last_op['preprocess']+'_'+last_op['split']+'_'+'information'+'.json'
    with open (jsonfilename,'w') as obj:
        json.dump(data_shape,obj)
        
        
    