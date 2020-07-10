import pymysql
import os
import sys
import datetime
import pandas as pd
import matplotlib as mb
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei']


def GetAllnumber_age():
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor=db.cursor()
    sql="select count(user_ID) from info_for_display where age!=''"
    cursor.execute(sql)
    row = cursor.fetchone()
    all_number = int(row[0])
    cursor.close()
    db.close()
    return all_number

def TodayAddnumber_age(all_number):
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()
    current_time=datetime.datetime.now()
    year1=current_time.year
    month1=current_time.month
    date1=current_time.day
    sql="select count(user_ID) from info_for_display where year='%s' and month='%s'and day='%s' and age!=''"%\
        (year1,month1,date1)
    cursor.execute(sql)
    row = cursor.fetchone()
    today_number=int(row[0])
    add_number=today_number #all_number-today_number
    cursor.close()
    db.close()
    return add_number


def GetAge():
    list_age=[['0-9',0],['10-19',0],['20-29',0],['30-39',0],['40-49',0],['50-59',0],['60-69',0],['70-79',0],['80-89',0],['90-99',0],['100以上',0]]
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()

    cursor.execute("select count(user_ID) from info_for_statistic where age>-1 and age<10")
    row = cursor.fetchone()
    number = row[0]
    list_age[0][1]=number

    cursor.execute("select count(user_ID) from info_for_statistic where age>9 and age<20")
    row = cursor.fetchone()
    number = row[0]
    list_age[1][1] = number

    cursor.execute("select count(user_ID) from info_for_statistic where age>19 and age<30")
    row = cursor.fetchone()
    number = row[0]
    list_age[2][1] = number

    cursor.execute("select count(user_ID) from info_for_statistic where age>29 and age<40")
    row = cursor.fetchone()
    number = row[0]
    list_age[3][1] = number

    cursor.execute("select count(user_ID) from info_for_statistic where age>39 and age<50")
    row = cursor.fetchone()
    number = row[0]
    list_age[4][1] = number

    cursor.execute("select count(user_ID) from info_for_statistic where age>49 and age<60")
    row = cursor.fetchone()
    number = row[0]
    list_age[5][1] = number

    cursor.execute("select count(user_ID) from info_for_statistic where age>59 and age<70")
    row = cursor.fetchone()
    number = row[0]
    list_age[6][1] = number

    cursor.execute("select count(user_ID) from info_for_statistic where age>69 and age<80")
    row = cursor.fetchone()
    number = row[0]
    list_age[7][1] = number

    cursor.execute("select count(user_ID) from info_for_statistic where age>79 and age<90")
    row = cursor.fetchone()
    number = row[0]
    list_age[8][1] = number

    cursor.execute("select count(user_ID) from info_for_statistic where age>89 and age<100")
    row = cursor.fetchone()
    number = row[0]
    list_age[9][1] = number

    cursor.execute("select count(user_ID) from info_for_statistic where age>99")
    row = cursor.fetchone()
    number = row[0]
    list_age[10][1] = number

    cursor.close()
    db.close()

    return list_age

def DrawAge(list_age):
    list_x=[]
    list_y=[]
    for i in range(len(list_age)):
        list_x.append(list_age[i][0])
        list_y.append(list_age[i][1])

    x=range(len(list_y))
    y=list_y
    xticks1 = list_x
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    plt.bar(x,y, width=0.45, align='center', color='powderblue', alpha=0.9)
    plt.xticks(x, xticks1, size='medium')
    for a, b in zip(x, y):
        plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=10)
    plt.xlabel("年龄段")
    plt.ylabel("个数")
    path = os.getcwd()
    path = path + os.sep +'image'
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    plt.savefig(path + os.sep + 'age.png')
    plt.close()
    return path + os.sep + 'age.png'


'''all_num = GetAllnumber_age()
print(all_num)
num = TodayAddnumber_age(all_num)
print(num)
list = GetAge()
str = DrawAge(list)
print(str)'''

