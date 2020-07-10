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

def GetAllnumber_day():
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor=db.cursor()
    sql="select count(user_ID) from info_for_display where day!=''"
    cursor.execute(sql)
    row = cursor.fetchone()
    all_number = int(row[0])
    cursor.close()
    db.close()
    return all_number

def TodayAddnumber_day(all_number):
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()
    current_time=datetime.datetime.now()
    year1=current_time.year
    month1=current_time.month
    date1=current_time.day
    sql = "select count(user_ID) from info_for_display where year='%s' and month='%s' and day='%s' and day!=''" % \
          (year1, month1, date1)
    cursor.execute(sql)
    row = cursor.fetchone()
    today_number=int(row[0])
    add_number=today_number#all_number-today_number
    cursor.close()
    db.close()
    return add_number

def GetDay():
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()
    sql = "select ill_time,count(user_ID),year,month,day from info_for_display where ill_time!='' group by ill_time order by ill_time "
    cursor.execute(sql)
    row = cursor.fetchone()
    list_day = []
    while row is not None:
        list_sub = [row[0], row[1], row[2], row[3], row[4]]
        list_day.append(list_sub)
        row = cursor.fetchone()
    # day_s_tu = cursor.fetchall()
    cursor.close()
    db.close()
    # day_s = list(day_s_tu)
    # print(len(day_s))
    for i in list_day:
        for j in list_day:
            if (int(i[2]) < int(j[2])) or (int(i[2]) == int(j[2]) and int(i[3]) < int(j[3])) or (
                    int(i[2]) == int(j[2]) and int(i[3]) == int(j[3]) and int(i[4]) < int(j[4])):
                temp = i[0]
                i[0] = j[0]
                j[0] = temp
                temp1 = i[1]
                i[1] = j[1]
                j[1] = temp1
                temp2 = i[2]
                i[2] = j[2]
                j[2] = temp2
                temp3 = i[3]
                i[3] = j[3]
                j[3] = temp3
                temp4 = i[4]
                i[4] = j[4]
                j[4] = temp4
    print(list_day)
    day_results = []
    print(list_day)
    for i in range(len(list_day)):
        if (list_day[i][2] != '2019' or int(list_day[i][3]) > 11):
            day_results.append((list_day[i][0], list_day[i][1]))

    return day_results

def DrawDay(day_results):
    list_x = []
    list_y = []
    for i in range(len(day_results)):
        list_x.append(day_results[i][0])
        list_y.append(day_results[i][1])

    params = {
        'figure.figsize': '10, 5'
    }
    plt.rcParams.update(params)
    x = range(len(list_y))
    y = list_y
    xticks1 = list_x
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    plt.bar(x, y, width=0.45, align='center', color='powderblue', alpha=0.9)
    plt.xticks(x, xticks1, size='small')
    for a, b in zip(x, y):
        plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=10)
    plt.xticks(rotation=45)
    plt.xlabel("每天")
    plt.ylabel("个数")
    path = os.getcwd()
    path = path + os.sep +'image'
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    plt.savefig(path + os.sep + 'day.png')
    plt.close()
    return path + os.sep + 'day.png'

'''all = GetAllnumber_day()
print(all)
today = TodayAddnumber_day(all)
list1 = GetDay()
print(list1)
str1 = DrawDay(list1)
print(str1)'''
