from selenium import webdriver, common
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import os
import time
import random
import sys
import math


class TechnologyPower:
    def __init__(self, username, pwd):
        self.startUrl = 'https://login.dingtalk.com/login/index.htm?goto=https%3A%2F%2Foapi.dingtalk.com%2Fconnect%2Foauth2%2Fsns_authorize%3Fappid%3Ddingoankubyrfkttorhpou%26response_type%3Dcode%26scope%3Dsnsapi_login%26redirect_uri%3Dhttps%3A%2F%2Fpc-api.xuexi.cn%2Fopen%2Fapi%2Fsns%2Fcallback'
        self.homeUrl = 'https://www.xuexi.cn/'
        self.isLogin = False
        option = webdriver.ChromeOptions()
        # option.add_argument("headless")
        option.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.images": 2})
        self.browser = webdriver.Chrome(options=option)
        self.articleListHandle = ''
        self.videoListHandle = ''

        try:
            while self.isLogin == False:
                self.login(username, pwd)
                time.sleep(2)
                if self.browser.current_url != 'https://pc.xuexi.cn/points/my-study.html':
                    print('登录失败，可能是出现了验证码，建议确认账号密码或等待重试')
                    time.sleep(4)
                else:
                    print('登录成功')
                    self.isLogin = True
            # 阅读文章积分
            aritcleCount = 8
            self.jumpToHome()
            time.sleep(2)
            self.openArticleList()
            time.sleep(8)
            for i in range(aritcleCount):
                time.sleep(2)
                try:
                    self.watchArticle(i)
                except:
                    print('第 d% 篇文章没能阅读成功' % i)
                    aritcleCount = aritcleCount + 1
            # 看视频计分
            # self.browser.set_window_size(1280, 10000)  # 设定窗口大小，服务于后面的绝对定位点击
            time.sleep(2)
            self.jumpToHome()
            time.sleep(2)
            self.openVideoList()
            for i in range(8):
                time.sleep(2)
                self.watchVideo(i)
        except Exception as e:
            self.browser.close()
            self.browser.quit()
            print(e)

    def login(self, username, pwd):
        print('进入登录页')
        self.browser.get(self.startUrl)

        self.browser.execute_script(
            'document.getElementById("mobile").style.display="block";')
        self.browser.execute_script(
            'document.getElementById("pwd").style.display="block";')
        ActionChains(self.browser).move_by_offset(0, 0).move_by_offset(
            100, 100).move_by_offset(70, 70).perform()
        mobileIptDom = self.browser.find_element_by_id('mobile')
        pwdIptDom = self.browser.find_element_by_id('pwd')
        loginIptDom = self.browser.find_element_by_id('loginBtn')

        mobileIptDom.send_keys(username)
        pwdIptDom.send_keys(pwd)
        loginIptDom.click()

    def jumpToHome(self):
        self.browser.execute_script(
            'window.location.href="' + self.homeUrl + '"')

    def openArticleList(self):
        self.browser.execute_script(
            'document.getElementsByClassName("linkSpan")[0].click()')
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])
        self.articleListHandle = self.browser.current_window_handle

    def watchArticle(self, index):
        articleList = self.browser.find_elements_by_class_name(
            'text-link-item-title')
        ActionChains(self.browser).send_keys(Keys.SPACE)
        articleList[index + 1].click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        if self.browser.title == '内容详情':
            self.browser.refresh()
            time.sleep(5)
        print('开始文章第'+str(index+1)+'篇：' + self.browser.title)
        start = time.time()
        self.browser.execute_script('window.scrollTo(0, window.innerHeight)')
        for i in range(70):
            key = Keys.DOWN
            ActionChains(self.browser).key_down(key).perform()
            time.sleep(2)
        self.browser.close()
        self.browser.switch_to.window(self.articleListHandle)
        end = time.time()
        print('耗时：')
        print(end - start)
        print('\n')
        time.sleep(3)

    def openVideoList(self):
        logoDom = self.browser.find_elements_by_class_name('center-item')[0]
        logoDom.click()
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])
        self.videoListHandle = self.browser.current_window_handle
        time.sleep(2)
        # self.browser.find_elements_by_class_name('tab-wrapper')[11].click()
        # time.sleep(5)
        self.browser.find_element_by_class_name('list').click()

    def watchVideo(self, index):
        videoList = self.browser.find_elements_by_class_name(
            'text-link-item-title')
        videoList[index].click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        if(self.browser.title == '视频播放'):
            print('刷新试试↓↓↓')
            self.browser.refresh()
            time.sleep(3)
            self.browser.find_element_by_class_name('outter').click()
        print('开始视频：' + self.browser.title)
        start = time.time()
        time.sleep(2)
        self.browser.execute_script(
            'document.getElementsByClassName("prism-controlbar")[0].style.display="block"')
        time.sleep(4)
        totalTime = self.browser.find_element_by_class_name(
            'duration').text
        print('时长：' + totalTime)

        current_time = '00:00'
        while(current_time != self.browser.find_element_by_class_name('duration').text):
            key = Keys.DOWN
            if random.random() > 0.5:
                key = Keys.UP
            ActionChains(self.browser).key_down(key).perform()

            current_time = self.browser.find_element_by_class_name(
                'current-time').text
            sys.stdout.write('\r')
            sys.stdout.write("%s%% |%s" % (math.floor(self.dateToInt(current_time)/self.dateToInt(totalTime) * 100),
                                           math.floor(self.dateToInt(current_time)/self.dateToInt(totalTime) * 100)*'#'))
            sys.stdout.flush()
            time.sleep(2)
        time.sleep(6)

        self.browser.execute_script(
            'document.getElementsByClassName("prism-controlbar")[0].style.display="block"')
        print('\n')
        print('结束时视频时长：' + self.browser.find_element_by_class_name('current-time').text)
        self.browser.close()
        self.browser.switch_to.window(self.videoListHandle)
        end = time.time()
        print('耗时：')
        print(end - start)
        print('\n')
        time.sleep(3)

    def dateToInt(self, date):
        r = 0
        try:
            r = int(date.split(':')[0]) * 60 + int(date.split(':')[1])
        except Exception as e:
            print(e)
            print(date)
        return r


username = ''
pwd = ''
if os.path.exists('./passport'):
    f = open('./passport', 'r')
    data = f.read().split('|')
    username = data[0]
    pwd = data[1]
else:
    username = input('输入钉钉账号: ')
    pwd = input('输入钉钉密码: ')
myTechnologyPower = TechnologyPower(username, pwd)
