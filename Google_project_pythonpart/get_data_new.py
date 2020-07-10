'''
    author:Jiaxin Zheng
    data:2020/5/28
    function:从微博移动端的肺炎求助超话中获取文本及数据
             并初步处理
'''

import os
import csv
import re
import requests
from urllib.request import urlretrieve
from selenium import webdriver
from lxml import etree
import time,random
import pymysql

def output(etree_html,driver,csv_writer,all_num):



    '''获得有效装载帖子的列表'''
    vaild_list=driver.find_elements_by_xpath("//div[@class='card card11 ctype-2']/div/div[@class='card-list']")
    print(len(vaild_list))
    
    num=0
    all_info=[]
    for tlist in vaild_list:
        all_card=tlist.find_elements_by_xpath("//div[contains(@class,'card m-panel card9')]")

        tnum=0
        print(len(all_card))
        print('=========')
        
        ''' 遍历帖子'''
        for card in all_card:
            
            print('++++++++++++++++++++++++++++++++++++++++++++++++++')
            '''获得帖子的标头'''
            user_name=card.find_element_by_class_name("m-text-cut").text
            release_time=card.find_element_by_class_name("time").text
            
            print("求助人：%s"%user_name)
            # print("release_time：%s"%release_time)
            
            
            '''获得帖子的文章（文字及图片）'''
            article=card.find_element_by_class_name("weibo-main")
            article_all=article.find_element_by_class_name("weibo-text")#显示文章及隐藏的全文
            article_ptext= article_all.text

            # print("article_ptext：%s"%article_ptext)
            # print("article的长度：%d"%len(article_ptext))

            save=0
            

            '''获取隐藏全文'''
            if len(article_ptext)>6:
                # 在隐藏全文的情况下
                if article_ptext.find("...全文",len(article_ptext)-5,len(article_ptext))!=-1:
                    
                    article_atext=article_all.find_element_by_xpath(".//a[contains(text(),'全文')]").get_attribute('href')
                    print("文章的链接为：%s"%article_atext)
                    
                    #获取隐藏全文
                    article_htext = requests.get(url=article_atext).text
                    all_page = re.findall('.*?"text": "(.*?)",.*?', article_htext)[0]
                    comment_text = re.sub('<(S*?)[^>]*>.*?|<.*? />', '', all_page) #正则匹配掉html标签
                    #获取姓名
                    name=""

                    if "【姓名】" in all_page:
                        name = str(re.findall('.*?【姓名】(.*?)<', all_page)[0])
                    print(name)
                    
                    # if [user_name,name] not in all_info:
                        
                        # all_info.append([user_name,name])
                        
                        # print(comment_text)
                    csv_writer.writerow((user_name, release_time,comment_text))
                    try:
                        # 执行sql语句
                        sql = "INSERT INTO original_info_from_weibo(user_ID, \
                                                   release_time, content) \
                                                   VALUES ('%s', '%s', '%s')" % \
                              (user_name, release_time, article_ptext)
                        cur.execute(sql)
                        # 提交到数据库执行
                        conn.commit()

                    except:
                        # 如果发生错误则回滚
                        conn.rollback()
                        print("rollback!")
                    tnum=tnum+1
                    print(tnum)
                    if(tnum>=len(all_card)): 
                        return
                    # else:
                    #     return
                    
                else:
                    #获取姓名
                    # print(article_ptext)

                    beg=str(article_ptext).find("姓名",0,len(article_ptext))
                    end=str(article_ptext).find("【",beg+1,len(article_ptext))
                    name = str(article_ptext)[(beg+3):end]
                    if beg==-1:
                        name=""

                    # if [user_name,name] not in all_info:
                        # all_info.append([user_name,name])
                    csv_writer.writerow((user_name, release_time,article_ptext))
                    try:
                        # 执行sql语句
                        sql = "INSERT INTO original_info_from_weibo(user_ID, \
                                                   release_time, content) \
                                                   VALUES ('%s', '%s', '%s')" % \
                              (user_name, release_time, article_ptext)
                        cur.execute(sql)
                        # 提交到数据库执行
                        conn.commit()

                    except:
                        # 如果发生错误则回滚
                        conn.rollback()
                        print("rollback!")
                    tnum=tnum+1
                    print(tnum)
                    if(tnum>=len(all_card)): 
                        return

                    # else:
                    #     return
                # print(comment_text)
            '''获取图片'''
            #创建文件夹
            # os.makedirs('./image/', exist_ok=True)
            # article_piclist=article.find_elements_by_class_name("m-auto-list")
            # if len(article_piclist)!=0:
                
            #     imgfilepath='./image/'+user_name+'/'
            #     os.makedirs(imgfilepath, exist_ok=True)
                
            #     piclist=article_piclist[0].find_elements_by_class_name("m-auto-box")
            #     i=0
            #     for pic in piclist: 
            #         imgurl=pic.find_element_by_xpath(".//div[contains(@class,'m-img-box m-imghold-square')]/img").get_attribute('src')#从当前路径记得加.
            #         urlretrieve(imgurl , filename=imgfilepath+str(i)+'.png')
            #         i=i+1
            
            # print('++++++++++++++++++++++++++++++++++++++++++++++++++')
        # print(all_info)

            

    print('-----------------------')

def getdata():
    
    start = time.perf_counter()

    '''创建统计文件夹'''
    csvfilename='肺炎统计数据.csv'
    csvfile=open(csvfilename,'a',newline='',encoding='utf-8-sig')
    csv_writer=csv.writer(csvfile)
    csv_writer.writerow(('用户ID','发布时间', '内容'))#,'姓名', '年龄', '城市', '小区', '患病时间', '病情描述', '联系方式', '其他紧急联系人'))
    '''获取指定页面'''

    url='https://m.weibo.cn/p/index?containerid=1008084882401a015244a2ab18ee43f7772d6f&extparam=%E8%82%BA%E7%82%8E%E6%82%A3%E8%80%85%E6%B1%82%E5%8A%A9&luicode=10000011&lfid=100103type%3D1%26q%3D%E8%82%BA%E7%82%8E%E6%B1%82%E5%8A%A9%E8%B6%85%E8%AF%9D'
    '''控制浏览器'''

    # driver.implicitly_wait(5)
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument('--proxy--server=112.84.55.122:9999')#使用代理IP
    chrome_option.add_argument('--no-sandbox')
    chrome_option.add_argument('--disable-dev-shm-usage')
    chrome_option.add_argument('--headless')
    chrome_option.add_argument('blink-settings=imagesEnabled=false')
    chrome_option.add_argument('--disable-gpu')
    driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_option)
    driver.get(url)
    driver.implicitly_wait(10)#等待10秒进行登录
    
    '''获取帖子数'''

    #  vaild_list=driver.find_elements_by_xpath
    page_cover=driver.find_element_by_class_name('page-cover')
    info=page_cover.find_element_by_class_name('m-text-cut').text
    beg=str(info).find("帖子",0,len(info))
    end=str(info).find("粉丝",beg+1,len(info))
    all_num = int(str(info)[(beg+2):end])

    # all_num=50
    # 超过10个就要刷新

    '''显示所有页面'''
    if int(all_num) > 10:
        page_num=int(int(all_num)/10)
        js_operate="var q=document.documentElement.scrollTop=10000000"
        for i in range(page_num):
            driver.execute_script(js_operate)
            time.sleep(random.uniform(0, 1.5))
    '''对页面数据进行提取'''
    page_sourse=driver.page_source
    etree_html=etree.HTML(page_sourse)
    output(etree_html,driver,csv_writer,all_num)
    
    end = time.perf_counter()
    t=end-start

    print("Runtime is ：",t)
    driver.quit()
try:
    conn=pymysql.connect(
        host='rm-2zes6jqt7pe0cjy73125010.mysql.rds.aliyuncs.com',
        port=3306,
        user='insert_data',
        passwd='insert_data729',
        db='medical_user_info',
        charset='UTF8MB4'
    )
    cur=conn.cursor()
    cur.execute('drop table if exists original_info_from_weibo;')
    create_table_sql = '''
        CREATE TABLE original_info_from_weibo(
            user_ID VARCHAR(50) DEFAULT '',
            release_time VARCHAR(20) DEFAULT '',
            content VARCHAR(500) DEFAULT '')engine=innodb DEFAULT CHARACTER set UTF8MB4;
    '''
    cur.execute(create_table_sql)
    print('创建数据库表成功！')
    getdata()
except pymysql.Error as e:
    print('mysql.Error: ',e.args[0],e.args[1])
print("extracting data finished")

