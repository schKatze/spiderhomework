#!/user/bin/python3
# -*- coding = utf-8 -*-
# @Time : 2021/3/21
# @Author : 郑煜辉
# @File : test1
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import json
import codecs

# driver = webdriver.Firefox()
# res=driver.get("https://pintia.cn/api/problem-sets/14/problems/733")
# data = res.text
# print(data)
payload = {'key1': 'value1', 'key2': 'value2'}
headers = {
    'Host': 'pintia.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.146 Safari/537.36',
    'Accept': 'application/json;charset=UTF-8',
    'Cookie': '_ga=GA1.2.592894529.1582188659; _9755xjdesxxd_=32; __snaker__captcha=snqmc7MZHM1C4F3y; '
              'gdxidpyhxdE=Xwg4ZrMhoiZTkZGozSyjBij%5CJ5WS%5CIqVTOxAnUtaiVhlebKCASRSgp6n3'
              '%2BEQmKTfvSjYCEIj0PwEfPkdmjGsg83%5CXokL2hafAqSz%2F0NsZtwRQKT%5C8vWzK0qJe49v1vH8ONKPzyBhrB5A%2B%5CZwt'
              '%2FTcux0yYdnTNdBbSjBV54avVL%5CcHjHs%3A1597548356066; '
              '__gads=ID=4d43aea6bdcc8402-2250b33771c6005e:T=1616041663:RT=1616041663:S=ALNI_Mb2eHV_'
              '-0fE9jIjaByMiHmu6u9x-A; _gid=GA1.2.391097635.1616256328; JSESSIONID=0184424C37C152E19C839EC4F827A8B5 '
}


def getDriver(url):
    driver = webdriver.firefox()
    driver.get(url)
    return driver


def getProLists(driver, ulists):
    wait = WebDriverWait(driver, 3)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "DataTableContainer_3cQiI")))
    pros = driver.find_elements_by_css_selector(
        "div.DataTableContainer_3cQiI > table > tbody > tr > td:nth-child(3) > a")
    for pro in pros:
        ulists.append([pro.text, pro.get_attribute('href')])
    print(ulists)
    return ulists


if __name__ == '__main__':
    url = 'https://pintia.cn/problem-sets/14/problems/type/6'
    driver = getDriver(url)
    ulists = []
    getProLists(driver, ulists)
    pass
