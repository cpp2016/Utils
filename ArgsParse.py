#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/11/22 10:49 下午
# @Author : gaofujie
# @File : ArgsParse.py
# @namespace scheme: MyFile, MyClass, myFunc, my_vaR, CONST
# @var name type: classC, dictD, listL, stringS, intI, floatF, tupleT


# imports
import argparse
## 生成参数分析器
parser = argparse.ArgumentParser('main')
## 参数
parser.add_argument('--data_home', type=str,
                    default='/data/data/pkdd-15-predict-taxi-service-trajectory-i', help='data home path')
parser.add_argument('--log_path',  type=str,
                    default='./log.TaxiDataProcess', help='log of taxi data process')
parser.add_argument('--data_home1', type=str,
                    default='/data/data/pkdd-15-predict-taxi-service-trajectory-i', help='data home path')
parser.add_argument('--log_path2',  type=str,
                    default='./log.TaxiDataProcess', help='log of taxi data process')
parser.add_argument('--data_home3', type=str,
                    default='/data/data/pkdd-15-predict-taxi-service-trajectory-i', help='data home path')
parser.add_argument('--log_path4',  type=str,
                    default='./log.TaxiDataProcess', help='log of taxi data process')
parser.add_argument('--data_home5', type=str,
                    default='/data/data/pkdd-15-predict-taxi-service-trajectory-i', help='data home path')
parser.add_argument('--log_path6',  type=str,
                    default='./log.TaxiDataProcess', help='log of taxi data process')
parser.add_argument('--data_home7', type=str,
                    default='/data/data/pkdd-15-predict-taxi-service-trajectory-i', help='data home path')
parser.add_argument('--log_path8',  type=str,
                    default='./log.TaxiDataProcess', help='log of taxi data process')
parser.add_argument('--data_home9', type=str,
                    default='/data/data/pkdd-15-predict-taxi-service-trajectory-i', help='data home path')
parser.add_argument('--log_path10',  type=str,
                    default='./log.TaxiDataProcess', help='log of taxi data process')
parser.add_argument('--data_home11', type=str,
                    default='/data/data/pkdd-15-predict-taxi-service-trajectory-i', help='data home path')
parser.add_argument('--log_path12',  type=str,
                    default='./log.TaxiDataProcess', help='log of taxi data process')
## args
args = parser.parse_args()
print('\n******* Args List Begin **********')
print(' {:<5} {:<12} {:<6} {}'.format('RANK', 'NAME', 'TYPE', 'VALUE'))
for i, arg in enumerate(vars(args)):
    value = getattr(args,arg)
    print(' {:<5} {:<12} {:<6} {}'.format(i+1, arg, type(value).__name__, value))
print('******* Args List End **********\n')

# paras

# log


# classes


# funcs


if __name__ == '__main__':
    pass