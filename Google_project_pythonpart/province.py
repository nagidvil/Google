import pymysql
import sys
import os
import datetime
import pandas as pd
import matplotlib as mb
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei']

def GetAllnumber_province(pro):
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor=db.cursor()
    sql="select count(user_ID) from info_for_display where province='%s'"%(pymysql.escape_string(pro))
    cursor.execute(sql)
    row = cursor.fetchone()
    #all_number=int(cursor.rowcount)
    all_number = int(row[0])
    cursor.close()
    db.close()
    return all_number

def TodayAddnumber_province(all_number,pro):
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()
    current_time=datetime.datetime.now()
    year1=current_time.year
    month1=current_time.month
    date1=current_time.day
    sql="select count(user_ID) from info_for_display where year='%s'and month='%s' and day='%s' and province='%s'"%\
        (year1,month1,date1,pymysql.escape_string(pro))
    cursor.execute(sql)
    row = cursor.fetchone()
    today_number=int(row[0])
    add_number=today_number#all_number-today_number
    cursor.close()
    db.close()
    return add_number

def GetProvince(pro):
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()
    sql="select city,count(user_ID) from info_for_display where province='%s' group by city "%(pymysql.escape_string(pro))
    cursor.execute(sql)
    province_results_tu = cursor.fetchall()
    cursor.close()
    db.close()
    province_results=list(province_results_tu)
    return province_results

def DrawProvince(province_results,pro):
    list_x = []
    list_y = []
    for i in range(len(province_results)):
        list_x.append(province_results[i][0])
        list_y.append(province_results[i][1])
    params = {
        'figure.figsize': '10, 7'
    }
    plt.rcParams.update(params)
    x = range(len(list_y))
    y = list_y
    xticks1 = list_x
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    plt.bar(x, y, width=0.45, align='center', color='powderblue', alpha=0.9)
    plt.xticks(x, xticks1, size='medium')
    for a, b in zip(x, y):
        plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=10)

    plt.xlabel(pro)
    plt.ylabel("个数")
    path = os.getcwd()
    path = path + os.sep +'image'
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    plt.savefig(path + os.sep + pro+'.png')
    plt.close()
    return path + os.sep + pro+'.png'

'''num = GetAllnumber_province('湖北省')
print(num)
today = TodayAddnumber_province(num, '湖北省')
list1 = GetProvince('湖北省')
str1 = DrawProvince(list1,'湖北省')
print(str1)'''
