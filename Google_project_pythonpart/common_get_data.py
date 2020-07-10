'''
    author:Jiaxin Zheng
    data:2020/7/3
    function:通用网页爬虫数据
'''
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
def outInfo(text,filename):
    '''输出字符串为文件'''
    file = open(filename,'a')
    file.write(text)
    file.close()

def commonGetWebInfo(url):
    '''控制浏览器'''
    chrome_option=webdriver.ChromeOptions()
    chrome_option.add_argument('--proxy--server=112.84.55.122:9999')#使用代理IP
    chrome_option.add_argument('--no-sandbox')
    chrome_option.add_argument('--disable-dev-shm-usage')
    chrome_option.add_argument('--headless')
    chrome_option.add_argument('--disable-gpu')
    chrome_option.add_argument('blink-settings=imagesEnabled=false')
    driver = webdriver.Chrome(chrome_options=chrome_option)
    driver.get(url)
    #加载网页到底端
    js_operate="var q=document.documentElement.scrollTop=10000000"
    driver.execute_script(js_operate)
    
    page_sourse=driver.page_source
    etree_html=etree.HTML(page_sourse)
    
    all_text=driver.find_element_by_tag_name('body').text
    driver.quit()
    return all_text

def getNameList(seg_con):
    Nature = JClass("com.hankcs.hanlp.corpus.tag.Nature")
    name_list = []
    for term in seg_con:
        if term.nature == Nature.fromString("nr"):
            name_list.append(term.word)
    return name_list

def getDiseaseList(seg_con):
    Nature = JClass("com.hankcs.hanlp.corpus.tag.Nature")
    disease_set = set()
    disease_list = []
    for term in seg_con:
        if term.nature == Nature.fromString("nhd"):
            disease_set.add(term.word)
            #disease_list.append(term.word)
    for disease in disease_set:
        disease_list.append(disease)
    return disease_list

'''if __name__ == "__main__":
    url='http://www.zgdbjz.org.cn/home/help/qz.dbjz?p=1'
    #filename='webinfo.text'
    allInfo=commonGetWebInfo(url)
    seg_content = HanLP.segment(allInfo)
    # seg_content = HanLP.segment(content111)
    name_list = getNameList(seg_content)
    disease_list = getDiseaseList(seg_content)
    print(name_list)
    print(disease_list)
    #outInfo(allInfo,filename)'''
