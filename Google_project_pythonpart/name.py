import pymysql
import sys
import json
def GetProvinceName():
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()
    sql="select distinct province from info_for_display"
    cursor.execute(sql)
    row = cursor.fetchone()
    name_list = []
    while row is not None:
        if row[0]!='其他' and row[0]!='山东省':
            name_list.append(row[0])
        row = cursor.fetchone()
    #proname_results_tu = cursor.fetchall()
    cursor.close()
    db.close()
    #proname_results = list(proname_results_tu)
    return name_list

def GetCityName(pro):
    db = pymysql.connect(host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com', port=3306, user='insert_data',
                         passwd='insert_data729', db='medical_user_info', charset='UTF8MB4')
    cursor = db.cursor()
    sql="select province,city,count(city) from info_for_display where province='%s' group by city"%(pymysql.escape_string(pro))
    cursor.execute(sql)
    row = cursor.fetchone()
    result = []
    province_name = row[0]
    city_name = []
    while row is not None:
        city_name.append(row[1])
        row = cursor.fetchone()
    cursor.close()
    db.close()
    return city_name
    #cityname_results_tu = cursor.fetchall()
    #result.append(province_name)
    #result.append(city_name)

    #cityname_results = list(cityname_results_tu)
    #return result


'''pro_name = GetProvinceName()
citys_name = []
for i in pro_name:
    city_name = GetCityName(i)
    citys_name.append(city_name)
json_info = {'province': pro_name,'city':citys_name}
json_encode = json.dumps(json_info)
json_str = str(json.loads(json_encode))
print(json_info)'''