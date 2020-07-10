# -*- coding=utf-8 -*-
import socket
import pymysql
import os
import csv
import re
import requests
from urllib.request import urlretrieve
from selenium import webdriver
from lxml import etree
import time,random
import pandas as pd
import numpy as np
import sys
from pyhanlp import *
import jpype
import json

import common_get_data
import age
import year
import day
import month
import country
import province
import city
import name
import area
#获取自定义页面数据并分析
def common_get_data_info(url):
    print('get_info_common_get_data_info_function_success')
    allInfo = common_get_data.commonGetWebInfo(url)
    print('get_info_common_get_data_info_function_success')
    seg_content = HanLP.segment(allInfo)
    name_list = common_get_data.getNameList(seg_content)
    disease_list = common_get_data.getDiseaseList(seg_content)
    print(disease_list)
    common_data_json = {'name':name_list, 'disease':disease_list}
    common_data_json_encode = json.dumps(common_data_json)
    common_data_json_str = str(json.loads(common_data_json_encode))
    print(common_data_json_str )
    return common_data_json_str


def byte2int(num):#byte[]转为int型，用于获取Java发来的信息的长度，解决粘包问题
    real_num = (num[0] & 0xff)|((num[1] << 8) & 0xff00)|((num[2] << 24) >> 8)|(num[3] << 24)
    return real_num


def int2byte(num):#int型转为byte[]，将即将发送给Java的信息长度编码，解决粘包问题
    byte_num = bytearray()
    bnum1 = num & 0xff
    bnum2 = (num >> 8) & 0xff
    bnum3 = (num >> 16) & 0xff
    bnum4 = num >> 24
    byte_num = bytearray([bnum1,bnum2,bnum3,bnum4])
    return byte_num


#发送文件
def send_file(conn, filepath):
    while 1:
        if os.path.isfile(filepath):
            # 定义定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
            fileinfo_size = len(os.path.basename(filepath).encode())
            b_fileinfo_size = int2byte(fileinfo_size)
            conn.send(b_fileinfo_size)
            conn.send(os.path.basename(filepath).encode())
            file_size = os.path.getsize(filepath)
            b_file_size = int2byte(file_size)
            conn.send(b_file_size)
            # 定义文件头信息，包含文件名和文件大小
            # fhead = struct.pack('128sl', bytes(os.path.basename(filepath).encode('utf-8')), os.stat(filepath).st_size)
            # s.send(fhead)
            print('client filepath: {0}'.format(filepath))
            fp = open(filepath, 'rb')
            while 1:
                data = fp.read(1024)
                if not data:
                    print('{0} file send over...'.format(filepath))
                    break
                conn.send(data)
            # receipt_info = decode_command(conn)
        conn.close()
        break


def send_json(conn, json_info):
    size_of_json_info = len(json_info.encode())
    print(size_of_json_info)
    b_size_of_json_info = int2byte(size_of_json_info)
    conn.send(b_size_of_json_info)
    conn.sendall(json_info.encode())
    #conn.recv(4)
    #conn.close()

#解码java的命令，返回字符串类型命令
def decode_command(conn):
    szBuf = conn.recv(4)
    print(szBuf[0])
    #length_of_command = int.from_bytes(szBuf, byteorder='big', signed=True)
    length_of_command = byte2int(szBuf)
    print(length_of_command)
    if szBuf[0]!=length_of_command:
        return "illegal input,refuse to connect_845125"
    offset = 0
    content_command = b''
    if length_of_command > 1024:
        times_of_receive = length_of_command / 1024 + 1
        while times_of_receive > 0:
            if times_of_receive == 1:
                szBuf = conn.recv(length_of_command % 1024)
                content_command = content_command + szBuf
            else:
                szBuf = conn.recv(1024)
                content_command = content_command + szBuf
    else:
        szBuf = conn.recv(length_of_command)
        content_command = content_command + szBuf
    command = content_command.decode('utf-8')
    return command


#get_age_allnumber
def age_allnumber_function():
    all_num = age.GetAllnumber_age()
    all_num_json = {'number': all_num}
    all_num_json_encode = json.dumps(all_num_json)
    all_num_json_str = str(json.loads(all_num_json_encode))
    print(all_num_json_str)
    return all_num_json_str


#get_age_addnumber
def age_addnumber_function():
    all_num = age.GetAllnumber_age()
    num = age.TodayAddnumber_age(all_num)
    all_num_json = {'number': num}
    all_num_json_encode = json.dumps(all_num_json)
    all_num_json_str = str(json.loads(all_num_json_encode))
    print(all_num_json_str)
    return all_num_json_str

#get_age_results
def age_results_function():
    list1 = age.GetAge()
    str_name = []
    num = []
    for i in list1 :
        str_name.append(i[0])
        num.append(i[1])
    json_info = {'results_name':str_name,'results_num':num}
    json_encode = json.dumps(json_info)
    json_str = str(json.loads(json_encode))
    return json_str


#get_age_picture
def age_picture_function():
    list1 = age.GetAge()
    str1 = age.DrawAge(list1)
    return str1

#get_time_allnumber
def time_allnumber_function():
    all_num = year.GetAllnumber_year()
    all_num_json = {'number': all_num}
    all_num_json_encode = json.dumps(all_num_json)
    all_num_json_str = str(json.loads(all_num_json_encode))
    print(all_num_json_str)
    return all_num_json_str


#get_time_addnumber
def time_addnumber_function():
    all_num = year.GetAllnumber_year()
    num = year.TodayAddnumber_year(all_num)
    all_num_json = {'number': num}
    all_num_json_encode = json.dumps(all_num_json)
    all_num_json_str = str(json.loads(all_num_json_encode))
    print(all_num_json_str)
    return all_num_json_str


#get_year_results
def year_results_function():
    list1 = year.GetYear()
    str_name = []
    num = []
    for i in list1:
        str_name.append(i[0])
        num.append(i[1])
    json_info = {'results_name': str_name, 'results_num': num}
    json_encode = json.dumps(json_info)
    json_str = str(json.loads(json_encode))
    return json_str


#get_year_picture
def year_picture_function():
    list1 = year.GetYear()
    str1 = year.DrawYear(list1)
    return str1


#get_day_results
def day_results_function():
    list1 = day.GetDay()
    str_name = []
    num = []
    for i in list1:
        str_name.append(i[0])
        num.append(i[1])
    json_info = {'results_name': str_name, 'results_num': num}
    json_encode = json.dumps(json_info)
    json_str = str(json.loads(json_encode))
    return json_str


#get_day_picture
def day_picture_function():
    list1 = day.GetDay()
    str1 = day.DrawDay(list1)
    return str1


def GetMonth2019():

    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor=db.cursor()

    sql="select year,month,count(user_ID) from info_for_display where year=2019 and month!='' and month>10 group by month order by month"
    cursor.execute(sql)
    month2019_results_tu=cursor.fetchall()
    cursor.close()
    db.close()
    month2019_results=list(month2019_results_tu)
    return month2019_results

def GetMonth2020():
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()
    sql = "select year,month,count(user_ID) from info_for_display where year=2020 and month!='' group by month order by month"
    cursor.execute(sql)
    month2020_results_tu = cursor.fetchall()
    cursor.close()
    db.close()
    month2020_results=list(month2020_results_tu)
    return month2020_results
#get_month2019_results


def month2019_results_function():
    month2019_results = GetMonth2019()
    year = []
    month = []
    num = []
    for i in month2019_results:
        year.append(i[0])
        month.append(i[1])
        num.append(i[2])
    json_info = {'results_year': year, 'results_month': month, 'results_num': num}
    json_encode = json.dumps(json_info)
    json_str = str(json.loads(json_encode))
    return json_str

#get_month2020_results
def month2020_results_function():
    month2020_results = GetMonth2020()
    year = []
    month = []
    num = []
    for i in month2020_results:
        year.append(i[0])
        month.append(i[1])
        num.append(i[2])
    json_info = {'results_year': year, 'results_month': month, 'results_num': num}
    json_encode = json.dumps(json_info)
    json_str = str(json.loads(json_encode))
    return json_str


#get_month2019_picture
def month2019_picture_function():
    month2019_results = month.GetMonth2019()
    str1 = month.DrawMonth2019(month2019_results)
    return str1


#get_month2020_picture
def month2020_picture_function():
    month2020_results = month.GetMonth2020()
    str1 = month.DrawMonth2020(month2020_results)
    return str1


#get_country_allnumber
def country_allnumber_function():
    all_num = country.GetAllnumber_country()
    all_num_json = {'number': all_num}
    all_num_json_encode = json.dumps(all_num_json)
    all_num_json_str = str(json.loads(all_num_json_encode))
    print(all_num_json_str)
    return all_num_json_str


#get_country_addnumber
def country_addnumber_function():
    all_num = country.GetAllnumber_country()
    num = country.TodayAddnumber_country(all_num)
    all_num_json = {'number': num}
    all_num_json_encode = json.dumps(all_num_json)
    all_num_json_str = str(json.loads(all_num_json_encode))
    print(all_num_json_str)
    return all_num_json_str


#get_country_results
def country_results_function():
    list1 = country.GetCountry()
    str_name = []
    num = []
    for i in list1:
        str_name.append(i[0])
        num.append(i[1])
    json_info = {'results_name': str_name, 'results_num': num}
    json_encode = json.dumps(json_info)
    json_str = str(json.loads(json_encode))
    return json_str


#get_country_picture
def country_picture_function():
    list1 = country.GetCountry()
    str1 = country.DrawCountry(list1)
    return str1


#get_province_allnumber
def province_allnumber_function(pro_name):
    all_num = province.GetAllnumber_province(pro_name)
    all_num_json = {'number': all_num}
    all_num_json_encode = json.dumps(all_num_json)
    all_num_json_str = str(json.loads(all_num_json_encode))
    print(all_num_json_str)
    return all_num_json_str


#get_province_addnumber
def province_addnumber_function(pro_name):
    all_num = province.GetAllnumber_province(pro_name)
    num = province.TodayAddnumber_province(all_num, pro_name)
    all_num_json = {'number': num}
    all_num_json_encode = json.dumps(all_num_json)
    all_num_json_str = str(json.loads(all_num_json_encode))
    print(all_num_json_str)
    return all_num_json_str


#get_province_results
def province_results_function(pro_name):
    list1 = province.GetProvince(pro_name)
    str_name = []
    num = []
    for i in list1:
        str_name.append(i[0])
        num.append(i[1])
    json_info = {'results_name': str_name, 'results_num': num}
    json_encode = json.dumps(json_info)
    json_str = str(json.loads(json_encode))
    return json_str


#get_province_picture
def province_picture_function(pro_name):
    list1 = province.GetProvince(pro_name)
    str1 = province.DrawProvince(list1,pro_name)
    return str1


#get_city_allnumber
def city_allnumber_function(ci):
    all_num = city.GetAllnumber_city(ci)
    all_num_json = {'number': all_num}
    all_num_json_encode = json.dumps(all_num_json)
    all_num_json_str = str(json.loads(all_num_json_encode))
    print(all_num_json_str)
    return all_num_json_str


#get_city_addnumber
def city_addnumber_function(ci):
    all_num = city.GetAllnumber_city(ci)
    num = city.TodayAddnumber_city(all_num, ci)
    all_num_json = {'number': num}
    all_num_json_encode = json.dumps(all_num_json)
    all_num_json_str = str(json.loads(all_num_json_encode))
    print(all_num_json_str)
    return all_num_json_str


#get_city_results
def city_results_function(ci):
    list1 = city.GetCity(ci)
    str_name = []
    num = []
    for i in list1:
        str_name.append(i[0])
        num.append(i[1])
    json_info = {'results_name': str_name, 'results_num': num}
    json_encode = json.dumps(json_info)
    json_str = str(json.loads(json_encode))
    return json_str


#get_city_picture
def city_picture_function(ci):
    list1 = city.GetCity(ci)
    str1 = city.DrawCity(list1,ci)
    return str1

#get_province_allnamelist
def get_province_allnamelist_function():
    list1 = name.GetProvinceName()
    json_info = {'province': list1}
    json_encode = json.dumps(json_info)
    json_str = str(json.loads(json_encode))
    return json_str

#get_city_allnamelist
def get_city_allnamelist_function():
    pro_name = name.GetProvinceName()
    citys_name = []
    for i in pro_name:
        city_name = name.GetCityName(i)
        citys_name.append(city_name)
    json_info = {'province': pro_name, 'city': citys_name}
    json_encode = json.dumps(json_info)
    json_str = str(json.loads(json_encode))
    return json_str

#get_area_highgrade
def area_highgrade_function():
    result_area = area.GetAreaResults()
    list1 = area.GetDangerHighGrade(result_area)
    json_info = {'province': list1}
    json_encode = json.dumps(json_info)
    json_str = str(json.loads(json_encode))
    return json_str

#get_area_midgrade
def area_midgrade_function():
    result_area = area.GetAreaResults()
    list1 = area.GetDangerMidGrade(result_area)
    json_info = {'province': list1}
    json_encode = json.dumps(json_info)
    json_str = str(json.loads(json_encode))
    return json_str


#get_area_age_pic
def area_age_pic_function(pro):
    list_age = area.GetArea_age(pro)
    str1 = area.DrawArea_age(list_age)
    return str1

#get_area_city_pic
def area_city_pic_function(pro):
    list_city = area.GetArea_allcity(pro)
    str1 = area.DrawArea_allcity(list_city)
    return str1

#get_area_month_pic
def area_month_pic_function(pro):
    list_month = area.GetArea_month(pro)
    str1 = area.DrawArea_month(list_month)
    return str1


def dan_patient_function():
    list_of_patient = area.GetCriticalPatientResults()
    user = []
    r_time = []
    name = []
    age = []
    location = []
    ill_time = []
    phone_n1 = []
    phone_n2 = []
    content = []
    for row in list_of_patient:
        user.append(row[0])
        r_time.append(row[1])
        name.append(row[2])
        age.append(row[3])
        sub_str = re.sub(u"([^?？【】(),.，。=+~·、*%！!\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", row[7])
        location.append(sub_str)
        ill_time.append(row[8])
        phone_n1.append(row[13])
        phone_n2.append(row[14])
        sub_str = re.sub(u"([^?？【】(),.，。=+~·、*%！!\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "",row[12])
        content.append(sub_str )
    json_info = {'user_ID': user,'release_time':r_time, 'name':name,'age':age, 'location':location, 'ill_time':ill_time,'phone_num1':phone_n1,'phone_num2':phone_n2,'original_content':content}
    json_encode = json.dumps(json_info)
    json_str = str(json.loads(json_encode))
    #print(json_str)
    return json_str


def similar_patient_function(s_num):
    list_of_patient = area.GetCriticalPatientResults()
    list_of_similar = area.GetSimilarResults(int(s_num), list_of_patient)
    user = []
    r_time = []
    name = []
    age = []
    location = []
    ill_time = []
    phone_n1 = []
    phone_n2 = []
    content = []
    for row in list_of_similar:
        user.append(row[0])
        r_time.append(row[1])
        name.append(row[2])
        age.append(row[3])
        sub_str = re.sub(u"([^?？【】(),.，。=+~·、*%！!\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", row[7])
        location.append(sub_str)
        ill_time.append(row[8])
        phone_n1.append(row[13])
        phone_n2.append(row[14])
        sub_str = re.sub(u"([^?？【】(),.，。=+~·、*%！!\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "",row[12])
        content.append(sub_str )
    json_info = {'user_ID': user, 'release_time': r_time, 'name': name, 'age': age, 'location': location, 'ill_time': ill_time, 'phone_num1': phone_n1, 'phone_num2': phone_n2, 'original_content': content}
    json_encode = json.dumps(json_info)
    json_str = str(json.loads(json_encode))
    return json_str


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("create socket succ!")

    sock.setblocking(False)
    sock.bind(('172.29.184.23', 6666))
    print('bind socket succ!')

    sock.listen(10)
    print('listen succ!')
    while True:
        try:
            #      print("listen for client...")
            flag = 0
            conn, addr = sock.accept()
            print("get client")
            print(addr)
            conn.settimeout(30)
            command = decode_command(conn)
            print("recv:" + command)

#------------------统计分析-年龄--------------------------
            if command == 'get_age_allnumber':
                flag = 1
                allnumber_json = age_allnumber_function()
                send_json(conn, allnumber_json)
            if command =='get_age_addnumber':
                flag = 1
                addnumber_json = age_addnumber_function()
                send_json(conn, addnumber_json)
            if command == 'get_age_results':
                flag = 1
                age_info_json = age_results_function()
                send_json(conn, age_info_json)
            if command == 'get_age_picture':
                flag = 1
                agepic_path = age_picture_function()
                send_file(conn, agepic_path)
#-----------------统计分析-年龄--------------------------

#-----------------统计分析-时间-------------------------
            if command == 'get_time_allnumber':
                flag = 1
                allnumber_json = time_allnumber_function()
                send_json(conn, allnumber_json)
            if command == 'get_time_addnumber':
                flag = 1
                addnumber_json = time_addnumber_function()
                send_json(conn, addnumber_json)
            if command == 'get_year_results':
                flag = 1
                year_info_json = year_results_function()
                send_json(conn, year_info_json)
            if command == 'get_year_picture':
                flag = 1
                yearpic_path = year_picture_function()
                send_file(conn, yearpic_path)
            if command == 'get_month2019_results':
                flag = 1
                month2019_info_json = month2019_results_function()
                send_json(conn, month2019_info_json)
            if command == 'get_month2020_results':
                flag = 1
                month2020_info_json = month2020_results_function()
                send_json(conn, month2020_info_json)
            if command == 'get_month2019_picture':
                flag = 1
                month2019pic_path = month2019_picture_function()
                send_file(conn, month2019pic_path)
            if command == 'get_month2020_picture':
                flag = 1
                month2020pic_path = month2020_picture_function()
                send_file(conn, month2020pic_path)
            if command == 'get_day_results':
                flag = 1
                day_info_json = day_results_function()
                send_json(conn, day_info_json)
            if command == 'get_day_picture':
                flag = 1
                daypic_path = day_picture_function()
                send_file(conn, daypic_path)
#-------------------统计分析-时间-------------------------

#-------------------统计分析-地区-------------------------
            if command == 'get_country_allnumber':
                flag = 1
                allnumber_json = country_allnumber_function()
                send_json(conn, allnumber_json)
            if command =='get_country_addnumber':
                flag = 1
                addnumber_json = country_addnumber_function()
                send_json(conn, addnumber_json)
            if command == 'get_country_results':
                flag = 1
                country_info_json = country_results_function()
                send_json(conn, country_info_json)
            if command == 'get_country_picture':
                flag = 1
                countrypic_path = country_picture_function()
                send_file(conn, countrypic_path)

            if command == 'get_province_allnumber':
                flag = 1
                province_name = decode_command(conn)
                allnumber_json = province_allnumber_function(province_name)
                send_json(conn, allnumber_json)
            if command =='get_province_addnumber':
                flag = 1
                province_name = decode_command(conn)
                addnumber_json = province_addnumber_function(province_name)
                send_json(conn, addnumber_json)
            if command == 'get_province_results':
                flag = 1
                province_name = decode_command(conn)
                info_json = province_results_function(province_name)
                send_json(conn, info_json)
            if command == 'get_province_picture':
                flag = 1
                province_name = decode_command(conn)
                pic_path =  province_picture_function(province_name)
                send_file(conn, pic_path)

            if command == 'get_city_allnumber':
                flag = 1
                city_name = decode_command(conn)
                allnumber_json = city_allnumber_function(city_name)
                send_json(conn, allnumber_json)
            if command == 'get_city_addnumber':
                flag = 1
                city_name = decode_command(conn)
                addnumber_json = city_addnumber_function(city_name)
                send_json(conn, addnumber_json)
            if command == 'get_city_results':
                flag = 1
                city_name = decode_command(conn)
                info_json = city_results_function(city_name)
                send_json(conn, info_json)
            if command == 'get_city_picture':
                flag = 1
                city_name = decode_command(conn)
                pic_path = city_picture_function(city_name)
                send_file(conn, pic_path)

            if command =='get_province_allnamelist':
                flag = 1
                province_info_json = get_province_allnamelist_function()
                send_json(conn, province_info_json)
            if command =='get_city_allnamelist':
                flag = 1
                info_json = get_city_allnamelist_function()
                send_json(conn, info_json)
# ------------------统计分析-地区-------------------------
#---------------------地区预警-----------------------------
            if command == 'get_area_highgrade':
                flag = 1
                info_json = area_highgrade_function()
                send_json(conn, info_json)
            if command == 'get_area_midgrade':
                flag = 1
                info_json = area_midgrade_function()
                send_json(conn, info_json)
            if command == 'get_area_age_pic':
                flag = 1
                pro_name = decode_command(conn)
                pic_path = area_age_pic_function(pro_name)
                send_file(conn, pic_path)
            if command == 'get_area_city_pic':
                flag = 1
                pro_name = decode_command(conn)
                pic_path = area_city_pic_function(pro_name)
                send_file(conn, pic_path)
            if command == 'get_area_month_pic':
                flag = 1
                pro_name = decode_command(conn)
                pic_path = area_month_pic_function(pro_name)
                send_file(conn, pic_path)
# ---------------------地区预警-----------------------------
#----------------------危急患者-----------------------------
            if command == 'get_dan_patient':
                flag = 1
                info_json = dan_patient_function()
                send_json(conn, info_json)
            if command == 'get_similar_patient':
                flag = 1
                s_num = decode_command(conn)
                info_json = similar_patient_function(s_num)
                send_json(conn, info_json)
#----------------------危急患者-----------------------------
            #str_su = send_file(conn)
            #print(str_su)
            if command == 'getWebData':
                flag = 1
                url_web = decode_command(conn)
                print(url_web)
                send_data_json_str = common_get_data_info(url_web)
                send_json(conn, send_data_json_str)
                # conn.send(b"made")
            if flag == 0:
                print('input wrong command,try another one')
                conn.close()
            print("end of servive")
        except:
            pass
except:
    print("init socket error!")