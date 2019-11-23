第一个文件夹preprocess,处理选择数据集，进行数据预处理，单列可视化图，热力图的功能：
1、Choose_data.py
程序功能：
将原始的数据集，存放到指定位置并转换为CSV格式
命名为：	数据集名称+_Selected_ + data+.csv
	数据集名称+_Selected_ + Label+.csv
	数据集名称+_original__+information+.json
输入内容：
argv[1]:被选中的数据集名称   示例：PEMFC

输出内容：
将PEMFC_Selected_data.csv和PEMFC_Selected_Label.csv存放到save_data文件夹
将PEMFC_original__information.json存放到information文件夹中
******************************************************************************************
2、Scaler.py
程序功能：
将输入的数据集整体做标准化操作，存放到指定位置
命名为：	数据集名称+_Scaler_+data+.csv
	数据集名称+_Scaler_+information+.json

输入内容：
argv[1]:被选中的数据集名称   示例：PEMFC

输出内容：
将PEMFC_Scaler_data.csv存放到save_data文件夹
将PEMFC_Scaler_information.json存放到information文件夹中
******************************************************************************************
3、MinMaxScaler.py
程序功能：
将输入的数据集整体做标准化操作，存放到指定位置
命名为：	数据集名称+_MinMaxScaler_+data+.csv
	数据集名称+_MinMaxScaler_+information+.json

输入内容：
argv[1]:被选中的数据集名称   示例：PEMFC

输出内容：
将PEMFC_MinMaxScaler_data.csv存放到save_data文件夹
将PEMFC_MinMaxScaler_information.json存放到information文件夹中
******************************************************************************************
4、Column_view.py
程序功能：
进行单列可视化，并存放在指定位置
命名为：	数据集名称+_预处理方法_+ColView+.png

输入内容：
argv[1]:被选中的数据集名称   示例：PEMFC_Scaler

输出内容：
将PEMFC_Scaler_ColView.png存放到picture文件夹
******************************************************************************************
4、Heatmap_view.py
程序功能：
进行矩阵热力度展示，并存放在指定位置
命名为：	数据集名称+_预处理方法_+Heatmap+.png

输入内容：
argv[1]:被选中的数据集名称   示例：PEMFC_Scaler

输出内容：
将PEMFC_Scaler_Heatmap.png存放到picture文件夹
******************************************************************************************