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


def GetArea_age(pro):

    area_list_age = [['0-19', 0], ['20-39', 0], ['40-59', 0], ['60-79', 0], ['80-99', 0], ['100以上', 0]]
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()

    cursor.execute("select count(user_ID) from info_for_statistic where age>-1 and age<20 and province='%s'"%(pymysql.escape_string(pro)))
    row = cursor.fetchone()
    number = int(row[0])
    area_list_age[0][1] = number

    cursor.execute("select count(user_ID) from info_for_statistic where age>19 and age<40 and province='%s'"%(pymysql.escape_string(pro)))
    row = cursor.fetchone()
    number = int(row[0])
    area_list_age[1][1] = number

    cursor.execute("select count(user_ID) from info_for_statistic where age>39 and age<60 and province='%s'"%(pymysql.escape_string(pro)))
    row = cursor.fetchone()
    number = int(row[0])
    area_list_age[2][1] = number

    cursor.execute("select count(user_ID) from info_for_statistic where age>59 and age<80 and province='%s'"%(pymysql.escape_string(pro)))
    row = cursor.fetchone()
    number = int(row[0])
    area_list_age[3][1] = number

    cursor.execute("select count(user_ID) from info_for_statistic where age>79 and age<100 and province='%s'"%(pymysql.escape_string(pro)))
    row = cursor.fetchone()
    number = int(row[0])
    area_list_age[4][1] = number

    cursor.execute("select count(user_ID) from info_for_statistic where age>99 and province='%s'"%(pymysql.escape_string(pro)))
    row = cursor.fetchone()
    number = int(row[0])
    area_list_age[5][1] = number

    cursor.close()
    db.close()

    return area_list_age


def GetArea_allcity(pro):
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()
    sql = "select city,count(user_ID) from info_for_display where province='%s' group by city "%(pymysql.escape_string(pro))
    cursor.execute(sql)
    area_province_results_tu = cursor.fetchall()
    cursor.close()
    db.close()
    area_province_results = list(area_province_results_tu)
    return area_province_results

def GetArea_month(pro):
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()
    sql = "select month,count(user_ID) from info_for_display where year='2020' and province='%s' group by month order by month " % \
          (pymysql.escape_string(pro))
    cursor.execute(sql)
    area_month_results_tu = cursor.fetchall()
    cursor.close()
    db.close()
    area_month_results = list(area_month_results_tu)
    return area_month_results


def DrawArea_age(area_list_age):
    list_x = []
    list_y = []
    for i in range(len(area_list_age)):
        list_x.append(area_list_age[i][0])
        list_y.append(area_list_age[i][1])

    color = ['lightblue', 'plum', 'lightgreen', 'moccasin', 'lightsalmon', 'lemonchiffon', 'navajowhite']
    plt.axes(aspect=1)
    plt.pie(x=list_y, labels=list_x, autopct='%3.1f %%', colors=color)

    plt.title("地区年龄段分布图")
    path = os.getcwd()
    path = path + os.sep+'image'
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    plt.savefig(path + os.sep + 'areaage.png')
    plt.close()
    return path + os.sep + 'areaage.png'

def DrawArea_allcity(area_province_results):
    list_x = []
    list_y = []
    for i in range(0, len(area_province_results),1):
        list_x.append(area_province_results[i][0])
        list_y.append(area_province_results[i][1])
        print(list_x)
        print(list_y)

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
    plt.xlabel("市")
    plt.ylabel("个数")
    plt.title("地区各市分布图")
    path = os.getcwd()
    path = path + os.sep+'image'
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    plt.savefig(path + os.sep + 'areaallcity.png')
    plt.close()
    return path + os.sep + 'areaallcity.png'


def DrawArea_month(area_month_results):
    list_x = []
    list_y = []
    for i in range(len(area_month_results)):
        list_x.append(area_month_results[i][0])
        list_y.append(area_month_results[i][1])

    x=list_x
    y=list_y
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    plt.plot(x, y, "powderblue", marker='.', ms=10, label="a")
    for a, b in zip(x, y):
        plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=10)
    plt.xlabel("月份")
    plt.ylabel("个数")
    plt.title("地区各月份分布图")
    path = os.getcwd()
    path = path + os.sep + 'image'
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    plt.savefig(path + os.sep + 'areamonth.png')
    plt.close()
    return path + os.sep + 'areamonth.png'


def GetAreaResults():
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()
    sql="select province,count(distinct user_ID) from info_for_display group by province"
    cursor.execute(sql)
    results_area_tu = cursor.fetchall()
    cursor.close()
    db.close()
    results_area=list(results_area_tu)
    return results_area


def GetDangerHighGrade(results_area):
    list_highgrade=[]
    for i in range(len(results_area)):
        if results_area[i][1]>99:
            list_highgrade.append(results_area[i][0])

    return list_highgrade

def GetDangerMidGrade(results_area):
    list_midgrade=[]
    for i in range(len(results_area)):
        if 9<results_area[i][1]<100:
            list_midgrade.append(results_area[i][0])

    return list_midgrade



#相似病例
def GetSimilarResults(i,row):
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()

    cursor.execute("select * from info_for_display where age>70 and age<80 and district='%s' and ill_time!=''"%(pymysql.escape_string(row[i][6])))
    results_similar_tu=cursor.fetchall()
    results_similar = list(results_similar_tu)
    if len(results_similar) == 0:
        cursor.execute("select * from info_for_display where age>70 and age<80 and city='%s' and ill_time!=''" %\
    (pymysql.escape_string(row[i][5])))
        results_similar_tu = cursor.fetchall()
        results_similar = list(results_similar_tu)
    cursor.close()
    db.close()
    return results_similar


#危急患者
def GetCriticalPatientResults():
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()
    sql="select * from info_for_display where age>80 and province!='' and ill_time!=''"
    cursor.execute(sql)
    results_person_tu = cursor.fetchall()

    cursor.close()
    db.close()
    results_person=list(results_person_tu)

    return results_person
'''
list_area_age = GetArea_age('湖北省')
str1 = DrawArea_age(list_area_age)
list_city = GetArea_allcity('湖北省')
#print(list_city)
str2 = DrawArea_allcity(list_city)
list_month = GetArea_month('湖北省')
DrawArea_month(list_month)
area_list = GetAreaResults()
'''
#print(area_list)
#print(GetDangerHighGrade(area_list))
#print(GetDangerMidGrade(area_list))



'''results_person=GetCriticalPatientResults()
print(results_person)
for i in range(len(results_person)):
    print(GetSimilarResults(i,results_person))'''


