��һ���ļ���preprocess,����ѡ�����ݼ�����������Ԥ�������п��ӻ�ͼ������ͼ�Ĺ��ܣ�
1��Choose_data.py
�����ܣ�
��ԭʼ�����ݼ�����ŵ�ָ��λ�ò�ת��ΪCSV��ʽ
����Ϊ��	���ݼ�����+_Selected_ + data+.csv
	���ݼ�����+_Selected_ + Label+.csv
	���ݼ�����+_original__+information+.json
�������ݣ�
argv[1]:��ѡ�е����ݼ�����   ʾ����PEMFC

������ݣ�
��PEMFC_Selected_data.csv��PEMFC_Selected_Label.csv��ŵ�save_data�ļ���
��PEMFC_original__information.json��ŵ�information�ļ�����
******************************************************************************************
2��Scaler.py
�����ܣ�
����������ݼ���������׼����������ŵ�ָ��λ��
����Ϊ��	���ݼ�����+_Scaler_+data+.csv
	���ݼ�����+_Scaler_+information+.json

�������ݣ�
argv[1]:��ѡ�е����ݼ�����   ʾ����PEMFC

������ݣ�
��PEMFC_Scaler_data.csv��ŵ�save_data�ļ���
��PEMFC_Scaler_information.json��ŵ�information�ļ�����
******************************************************************************************
3��MinMaxScaler.py
�����ܣ�
����������ݼ���������׼����������ŵ�ָ��λ��
����Ϊ��	���ݼ�����+_MinMaxScaler_+data+.csv
	���ݼ�����+_MinMaxScaler_+information+.json

�������ݣ�
argv[1]:��ѡ�е����ݼ�����   ʾ����PEMFC

������ݣ�
��PEMFC_MinMaxScaler_data.csv��ŵ�save_data�ļ���
��PEMFC_MinMaxScaler_information.json��ŵ�information�ļ�����
******************************************************************************************
4��Column_view.py
�����ܣ�
���е��п��ӻ����������ָ��λ��
����Ϊ��	���ݼ�����+_Ԥ������_+ColView+.png

�������ݣ�
argv[1]:��ѡ�е����ݼ�����   ʾ����PEMFC_Scaler

������ݣ�
��PEMFC_Scaler_ColView.png��ŵ�picture�ļ���
******************************************************************************************
4��Heatmap_view.py
�����ܣ�
���о���������չʾ���������ָ��λ��
����Ϊ��	���ݼ�����+_Ԥ������_+Heatmap+.png

�������ݣ�
argv[1]:��ѡ�е����ݼ�����   ʾ����PEMFC_Scaler

������ݣ�
��PEMFC_Scaler_Heatmap.png��ŵ�picture�ļ���
******************************************************************************************