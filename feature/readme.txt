******************************************************************************************
文件夹feature,存放特征工程

1、split.py
程序功能：
将数据集划分为训练集和测试集，并将存放到save_data文件夹，保存为.csv格式
在op中指明操作
命名为：
	数据集名称+_+数据预处理方法+_+数据划分方法+_+traindata/testdata(采用交叉验证则有标号当前折数).csv

输入内容：
argv[1]:划分方法，可选：‘Hold-out’，‘CV’
argv[2]:方法参数，跟选中的方法相关，例子：‘0.6’，‘5’
若选中留出法，指定训练集比列，浮点数表示
若选中交叉验证，指定折数，整数表示

输出内容：

①将PEMFC_Scaler_CV_testdata_1.csv 或 PEMFC_Scaler_Hold-out_testdata.csv 存放到save_data文件夹
②将划分后的数据集大小信息 PEMFC_Scaler_CV_information.json
或 PEMFC_Scaler_Hold-out_information.json 存放到information文件夹
③修改information文件夹中的op_information
添加键：	‘split’:划分方法
	‘CV_parameter ’:若采用CV的参数
	‘Hold-out_parameter’：若采用留出法的参数
******************************************************************************************