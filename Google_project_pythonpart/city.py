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

def GetAllnumber_city(ci):
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor=db.cursor()
    sql="select count(user_ID) from info_for_display where city='%s'"%(pymysql.escape_string(ci))
    cursor.execute(sql)
    row = cursor.fetchone()
    all_number=int(row[0])
    cursor.close()
    db.close()
    return all_number

def TodayAddnumber_city(all_number,ci):
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()
    current_time=datetime.datetime.now()
    year1=current_time.year
    month1=current_time.month
    date1=current_time.day
    sql="select count(user_ID) from info_for_display where year='%s' and month='%s' and day='%s' and city='%s'"%\
        (year1,month1,date1,pymysql.escape_string(ci))
    cursor.execute(sql)
    row = cursor.fetchone()
    today_number=int(row[0])
    add_number=today_number#all_number-today_number
    cursor.close()
    db.close()
    return add_number

def GetCity(ci):
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()
    #更改数据库空值
    sql="update info_for_display set province = '其他' where user_ID!='' and province=''"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    sql = "update info_for_display set city = '其他' where user_ID!='' and city=''"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    sql="select district,count(user_ID) from info_for_display where city='%s' and district!='' group by district"%(pymysql.escape_string(ci))
    cursor.execute(sql)
    row = cursor.fetchone()
    city_re = []
    while row is not None:
            list_c = [row[0],row[1]]
            city_re.append(list_c)
            row = cursor.fetchone()

    #city_results_tu = cursor.fetchall()
    cursor.close()
    db.close()
    #city_results=list(city_results_tu)
    return city_re#city_results


def DrawCity(city_results,ci):
    list_x = []
    list_y = []
    for i in range(len(city_results)):
        list_x.append(city_results[i][0])
        list_y.append(city_results[i][1])

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
    plt.xticks(rotation=45)
    plt.xlabel(ci)
    plt.ylabel("个数")
    path = os.getcwd()
    path = path + os.sep +'image'
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    plt.savefig(path + os.sep + ci+'.png')
    plt.close()
    return path + os.sep + ci+'.png'

'''num = GetAllnumber_city('武汉市')
print(num)
today = TodayAddnumber_city(num,'武汉市')
list1 = GetCity('武汉市')
str1 = DrawCity(list1, '武汉市')
print(str1)'''

