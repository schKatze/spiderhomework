#!/user/bin/python3
# -*- coding = utf-8 -*-
# @Time : 2021/3/27
# @Author : 郑煜辉
# @File : extratest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time
import numpy
import cv2
import os


def getDriver(url):
    driver = webdriver.Firefox()
    driver.get(url)
    name = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    name.send_keys("1375747120@qq.com")
    password.send_keys("326ZyhLd53994")
    login_button = driver.find_element_by_tag_name("button")
    login_button.click()
    # 等待两秒，验证码加载完成
    time.sleep(2)
    # bg背景图片
    bg_img_src = driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/img[1]').get_attribute('src')
    # front可拖动图片
    front_img_src = driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/img[2]').get_attribute('src')
    # 保存图片
    with open("bg.jpg", mode="wb") as f:
        f.write(requests.get(bg_img_src).content)
    with open("front.jpg", mode="wb") as f:
        f.write(requests.get(front_img_src).content)
    # 将图片加载至内存
    bg = cv2.imread("bg.jpg")
    front = cv2.imread("front.jpg")
    # 将背景图片转化为灰度图片，将三原色降维
    bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
    # 将可滑动图片转化为灰度图片，将三原色降维
    front = cv2.cvtColor(front, cv2.COLOR_BGR2GRAY)
    front = front[front.any(1)]
    # 用cv算法匹配精度最高的xy值
    result = cv2.matchTemplate(bg, front, cv2.TM_CCOEFF_NORMED)
    # numpy解析xy，注意xy与实际为相反，x=y,y=x
    x, y = numpy.unravel_index(numpy.argmax(result), result.shape)
    # 找到可拖动区域
    div = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div[2]')
    # 拖动滑块，以实际相反的y值代替x
    ActionChains(driver).drag_and_drop_by_offset(div, xoffset=y // 0.946, yoffset=0).perform()
    # 至此成功破解验证码，由于算法问题，准确率不能达到100%，可能需要多运行1~2次

    # driver_1 = webdriver.Firefox()
    # driver_1.get('https://pintia.cn/problem-sets/14/problems/733')
    time.sleep(5)
    submit_pre = driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/div/div[2]/div["
                                              "2]/form/div/div/div/div/div/div[2]/div/div[6]/div[1]/div/div/div/div["
                                              "5]/div/pre/span/span")
    submit_pre.send_keys("1375747120@qq.com")
    return driver



if __name__ == '__main__':
    driver = getDriver(
        'https://pintia.cn/auth/login?redirect=https%3A%2F%2Fpintia.cn%2Fproblem-sets%2F14%2Fproblems%2F733')
