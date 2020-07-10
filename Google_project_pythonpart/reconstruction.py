#coding=utf-8
import pandas as pd
import numpy as np
import re
import csv
import sys
from pyhanlp import *
import jpype
import cpca
import datetime as dt
import pymysql


ruleofphonenum = re.compile(r"(1[35678]\d{9})")#re of phonenum
Nature = JClass("com.hankcs.hanlp.corpus.tag.Nature")
rule_of_name = re.compile("(?<=(【姓名】))(.*)(?=(【年龄】))")
ruleofdate_type1=re.compile(r"(\d{4})[-./\u5e74](\d{1,2})[-.\u6708](\d{1,2})")#re of infected date type1【患病时间】[\s\u65e5]
ruleofdate_type2=re.compile(r"(\d{1,2})[-./\u6708](\d{1,2})")#re of infected date type2【患病时间】[\s\u65e5]
ruleofbeingpurech = re.compile(r'[\u4e00-\u9fa5]*')
rule_of_location=re.compile(".*?【所在城市】(.*)【所在小区、社区】(.*)【患病时间】")


now_time = dt.datetime.now().strftime('%F')
time_today = re.search(ruleofdate_type1,now_time)
year_now = time_today.group(1)
month_now =time_today.group(2)
day_now = time_today.group(3)


def time_limitation(year,month,day):
    if int(year) > int(year_now) or int(year)<2015:
        return False
    if int(month)<1 or int(month) >12 or (int(year) ==int(year_now) and int(month)>int(month_now)):
        return False
    if int(day)<1 or int(day)>31 or (int(year) == int(year_now) and int(month) == int(month_now) and int(day>day_now)):
        return False
    return True


def extract_phonenum(content):
    phonenum = re.findall(ruleofphonenum, content)
    return [phonenum]


def extract_name(content):
    name = ''
    name_type1 = re.findall('.*?【姓名】(.*?)【年龄】', content)
    name1 = re.search(rule_of_name, content)
    if name1:
        name = name1.group(2)
    name_list = []
    if name_type1:    #name extraction
        if len(name_type1[0]) > 8:
            namediv = HanLP.segment(name_type1[0])
            n_list = ''
            count = 0
            for term in namediv:
                if term.nature == Nature.fromString("nr"):
                    if count == 0:
                        n_list = n_list + term.word
                    else:
                        n_list = n_list + '、' + term.word
                    count = count + 1
            if len(n_list) > 0:
                name = n_list

    else:
        seg_content = HanLP.segment(content)
        for term in seg_content:
            if term.nature == Nature.fromString("nr"):
                name_list.append(term.word)
        patientname = ''
        if len(name_list) > 0:
            patientname = name_list[0]
            name = patientname
    return [name]


def extract_age(content):
    age = ''
    age_original = re.findall('.*?【年龄】(.*?)【所在城市】', content)
    count_n = -1
    count_s = -1
    count_ = 0
    list_age = []
    count_age = 0
    flag_for_age = 0
    seg_content = HanLP.segment(content)
    if age_original:
        age_has_ch = re.search(ruleofbeingpurech, age_original[0])
        if age_has_ch:
            pure_num = HanLP.segment(age_original[0])
            for ii in pure_num:
                if ii.nature == Nature.fromString("m"):
                    age_int = int(ii.word)
                    if age_int > 120:
                        break
                    if flag_for_age == 0:
                        age = age + ii.word
                        flag_for_age = flag_for_age + 1
                    else:
                        age = age + ',' + ii.word

    else:
        for term in seg_content:
            if term.word == '年龄':
                end = count_age + 5
                if len(seg_content) < end:
                    end = len(count_age)

                for i in range(count_age, end, 1):
                    if seg_content[i].nature == Nature.fromString("m") and len(seg_content[i].word) < 3:
                        age = seg_content[i].word
                        flag_for_age = 1
                        break
                if flag_for_age == 1:
                    break
            if term.word == '岁':
                start = count_age - 5
                if start < 0:
                    start = 0
                for i in range(start, count_age, 1):
                    if seg_content[i].nature == Nature.fromString("m") and len(seg_content[i].word) < 3:
                        age = seg_content[i].word
                        flag_for_age = 1
                        break
                if flag_for_age == 1:
                    break
            count_age = count_age + 1
    return [age]


def extract_date(content):
    date = []
    illdate = re.search(ruleofdate_type1, content)
    year = 0
    month = 0
    day = 0
    if illdate:
        year = illdate.group(1)
        month = illdate.group(2)
        day = illdate.group(3)
    else:
        illdate = re.search(ruleofdate_type2, content)
        if illdate:
            year = 2020 #attention!
            month = illdate.group(1)
            day = illdate.group(2)
    mege_date = str(year) + '.' + str(month) + '.' + str(day)
    is_time_currect = time_limitation(year, month, day)
    if mege_date == '0.0.0' or is_time_currect == False:
        date.append('')
        date.append('')
        date.append('')
        date.append('')
    else:
        date.append(mege_date)
        date.append(year)
        date.append(month)
        date.append(day)
    return [date]


def extract_location(content):
    loc = ''
    loc_specify = ''
    province = ''
    city = ''
    district = ''
    flag_for_locsp_is_empty = 0
    list_loc = re.findall(rule_of_location, content)
    if list_loc:
        for i in list_loc[0]:
            loc_specify = loc_specify + i
    if loc_specify!='':
        df1 = cpca.transform([loc_specify], cut=False)
        flag_for_locsp_is_empty = 1
    seg_content = HanLP.segment(content)
    for term in seg_content:
        if term.nature == Nature.fromString("ns"):
            loc = loc+term.word
    if loc !='':
        df = cpca.transform([loc], cut=False)
        province = df.loc[0, '省']
        city = df.loc[0, '市']
        district = df.loc[0, '区']
        if flag_for_locsp_is_empty==1:
            if df1.loc[0, '省']!='':
                province = df1.loc[0, '省']
            if df1.loc[0, '市']!='':
                city = df1.loc[0, '市']
            if df1.loc[0, '区']!='':
                district = df1.loc[0, '区']
    list=[province, city, district, loc_specify]
    return [list]


'''
df = pd.read_csv('肺炎统计数据.csv')
with open("data.csv", "w", newline='',encoding='utf_8_sig') as f:
    fileWriter = csv.writer(f, delimiter=',')
    list1=["用户ID", "发布时间", "姓名", "年龄", "省", "市", "区", "地址", "患病时间", "年", "月", "日", "内容", "联系方式", "其他联系方式"]
    fileWriter.writerow(list1)
    for index, row in df.iterrows():
        content_ori = row['内容']
        #content =content_ori.replace('\n ','').replace('\r','')
        content = re.sub('\s+', "", content_ori)
        phone_num = extract_phonenum(content)
        if phone_num[0]:
            list_for_storage = []
            list_for_storage.append(row['用户ID'])
            list_for_storage.append(row['发布时间'])
            name = extract_name(content)
            list_for_storage.append(name[0])
            age = extract_age(content)
            list_for_storage.append(age[0])
            location_list = extract_location(content)
            for i in location_list[0]:
                list_for_storage.append(i)
            date_list = extract_date(content)
            for i in date_list[0]:
                list_for_storage.append(i)
            list_for_storage.append(content)
            if len(phone_num[0]) == 1:
                list_for_storage.append(phone_num[0][0])
            else:
                list_for_storage.append(phone_num[0][0])
                list_for_storage.append(phone_num[0][1])
            fileWriter.writerow(list_for_storage)
f.close()
'''
try:
    conn = pymysql.connect(
        host='rm-2zes6jqt7pe0cjy736o.mysql.rds.aliyuncs.com',
        port=3306,
        user='insert_data',
        passwd='insert_data729',
        db='medical_user_info',
        charset='UTF8MB4'
    )
    cur = conn.cursor()
    cur.execute('drop table if exists test_for_recon;')
    create_table_sql ='''
        CREATE TABLE test_for_recon(
            user_ID VARCHAR(50) DEFAULT '',
            release_time VARCHAR(20) DEFAULT '',
            name VARCHAR(20) DEFAULT '',
            age VARCHAR(20) DEFAULT '',
            province VARCHAR(10) DEFAULT '',
            city VARCHAR(10) DEFAULT '',
            district VARCHAR(30) DEFAULT '', 
            detailed_address VARCHAR(50) DEFAULT '',
            ill_time VARCHAR(20) DEFAULT '',
            year VARCHAR(5) DEFAULT '',
            month VARCHAR(5) DEFAULT '',
            day VARCHAR(5) DEFAULT '',
            content VARCHAR(500) DEFAULT '',
            phone_num_1 VARCHAR(15) DEFAULT '',
            phone_num_2 VARCHAR(15) DEFAULT '')engine=innodb DEFAULT CHARACTER set UTF8MB4;
    '''
    cur.execute(create_table_sql)
    print('创建数据库表test_for_recon成功！')
    try:


        sql = "select * from original_info_from_weibo"
        cur.execute(sql)
        row = cur.fetchone()
        cur_for_exe=conn.cursor()
        while row is not None:
            print(row[0])
            content_ori = row[2]
            content = re.sub('\s+', "", content_ori)
            phone_num = extract_phonenum(content)
            if phone_num[0]:
                list_for_storage = []
                list_for_storage.append(row[0])
                list_for_storage.append(row[1])
                name = extract_name(content)
                list_for_storage.append(name[0])
                age = extract_age(content)
                list_for_storage.append(age[0])
                location_list = extract_location(content)
                for i in location_list[0]:
                    list_for_storage.append(i)
                date_list = extract_date(content)
                for i in date_list[0]:
                    list_for_storage.append(i)
                list_for_storage.append(content)
                if len(phone_num[0]) == 1:
                    list_for_storage.append(phone_num[0][0])
                    list_for_storage.append('')
                else:
                    list_for_storage.append(phone_num[0][0])
                    list_for_storage.append(phone_num[0][1])

                try:
                    # 执行sql语句
                    sql1 = "INSERT INTO test_for_recon(user_ID ,\
                        release_time ,name ,age , province ,city ,district , detailed_address ,ill_time ,\
                        year ,month ,day ,content ,phone_num_1 ,phone_num_2 ) \
                        VALUES ('%s', '%s', '%s','%s', '%s', '%s','%s', '%s', '%s','%s', '%s', '%s','%s', '%s', '%s')" % \
                          (list_for_storage[0], list_for_storage[1], list_for_storage[2], list_for_storage[3], list_for_storage[4], list_for_storage[5]\
                           , list_for_storage[6], list_for_storage[7], list_for_storage[8], list_for_storage[9], list_for_storage[10], list_for_storage[11], list_for_storage[12]\
                           , list_for_storage[13], list_for_storage[14])
                    cur_for_exe.execute(sql1)
                    # 提交到数据库执行
                    conn.commit()

                except:
                    # 如果发生错误则回滚
                    conn.rollback()
                    print("rollback!")
                #fileWriter.writerow(list_for_storage)
            row = cur.fetchone()


    except pymysql.Error as e:
        print('mysql.Error: ', e.args[0], e.args[1])
except pymysql.Error as e:
    print('mysql.Error: ',e.args[0],e.args[1])