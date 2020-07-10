import pymysql
import sys
import datetime
import pandas as pd
import matplotlib as mb
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os
from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei']

def GetAllnumber_country():
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor=db.cursor()
    sql="select count(user_ID) from info_for_display where province!=''"
    cursor.execute(sql)
    row = cursor.fetchone()
    all_number=int(row[0])
    cursor.close()
    db.close()
    return all_number

def TodayAddnumber_country(all_number):
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()
    current_time=datetime.datetime.now()
    year1=current_time.year
    month1=current_time.month
    date1=current_time.day
    sql="select count(user_ID) from info_for_display where year='%s' and month='%s' and day='%s' and province!=''"%\
        (year1, month1, date1)
    cursor.execute(sql)
    row = cursor.fetchone()
    today_number = int(row[0])
    add_number=today_number#all_number-today_number
    cursor.close()
    db.close()
    return add_number

def GetCountry():
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()
    sql="select province,count(user_ID) from info_for_display group by province having province!=''"
    cursor.execute(sql)
    country_results_tu = cursor.fetchall()
    cursor.close()
    db.close()
    country_results=list(country_results_tu)
    return country_results

def DrawCountry(country_results):
    list_x = []
    list_y = []
    for i in range(len(country_results)):
        list_x.append(country_results[i][0])
        list_y.append(country_results[i][1])

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
    plt.xlabel('全国')
    plt.ylabel('个数')
    path = os.getcwd()
    path = path + os.sep +'image'
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    plt.savefig(path + os.sep + 'country.png')
    plt.close()
    return path + os.sep + 'country.png'

