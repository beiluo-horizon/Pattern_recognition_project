# -*- coding: utf-8 -*-
"""
@Created: Wed Jan 16 16:29:04 2019

@Author: And-ZJ

@Edited:

@Completed:

@Content:

    readme

"""

"""
数据文件说明：

(1) trainData500.txt
    静态方法的训练集样本，每行一个样本，每列一个特征。
    总共 500 个样本，52列
        500个正常样本

(2) trainLabel500FD.txt
    训练集 trainData500.txt 每行样本所对应的标签。
    用于故障检测。
    标签 0 表示正常的样本
    标签 1 表示故障的样本，21 类故障都用标签 1。下同。

(3) trainLabel500FC.txt
    训练集 trainData500.txt 每行样本所对应的标签。
    用于故障诊断。
    标签 0 表示正常的样本
    标签 i 标签故障 i 的样本，i 取值范围 1-21。下同。



(4) testData21120.txt
    静态方法的测试集样本，每行一个样本，每列一个特征。
    总共 21120 个样本，52列
        960+160*21=4320 个正常样本
        800*21=16800 个故障样本

(5) testLabel21120FD.txt
    训练集 testData21120.txt 每行样本所对应的标签。
    用于故障检测。

(6) testLabel21120FC.txt
    训练集 testData21120.txt 每行样本所对应的标签。
    用于故障诊断。



(7) trainData10580.txt
    静态方法的训练集样本，每行一个样本，每列一个特征。
    总共 10580 个样本，52列
        500 个正常样本
        480*21=16800 个故障样本

(8) trainLabel10580FD.txt
    训练集 trainData10580.txt 每行样本所对应的标签。
    用于故障检测。

(9) trainLabel10580FC.txt
    训练集 trainData10580.txt 每行样本所对应的标签。
    用于故障诊断。



"""