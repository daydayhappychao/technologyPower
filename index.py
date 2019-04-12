from selenium import webdriver, common
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
import math


class TechnologyPower:
    def __init__(self, username, pwd):
        self.startUrl = 'https://login.dingtalk.com/login/index.htm?goto=https%3A%2F%2Foapi.dingtalk.com%2Fconnect%2Foauth2%2Fsns_authorize%3Fappid%3Ddingoankubyrfkttorhpou%26response_type%3Dcode%26scope%3Dsnsapi_login%26redirect_uri%3Dhttps%3A%2F%2Fpc-api.xuexi.cn%2Fopen%2Fapi%2Fsns%2Fcallback'
        self.homeUrl = 'https://www.xuexi.cn/'
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        option.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.images": 2})
        self.browser = webdriver.Chrome(options=option)
        self.articleListHandle = ''
        self.videoListHandle = ''
        self.login(username, pwd)
        # 阅读文章积分
        time.sleep(2)
        self.jumpToHome()
        time.sleep(2)
        self.openArticleList()
        for i in range(6):
          time.sleep(2)
          self.watchArticle(2 * i - 1)
        # 看视频计分
        # self.browser.set_window_size(1280, 10000)  # 设定窗口大小，服务于后面的绝对定位点击
        time.sleep(2)
        if self.browser.current_url != 'https://pc.xuexi.cn/points/my-study.html':
            raise Exception('登录失败，可能是出现了验证码，建议确认账号密码或重试')
        else:
            print('登录成功')
        self.jumpToHome()
        time.sleep(2)
        self.openVideoList()
        for i in range(6):
            time.sleep(2)
            self.watchVideo(i)

    def login(self, username, pwd):
        print('进入登录页')
        self.browser.get(self.startUrl)

        self.browser.execute_script(
            'document.getElementById("mobile").style.display="block";')
        self.browser.execute_script(
            'document.getElementById("pwd").style.display="block";')

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
        # logoDom = self.browser.find_elements_by_class_name('div-background-img-stretching')[2]
        logoDom = self.browser.find_elements_by_class_name('word-item')[29]
        logoDom.click()
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])
        self.articleListHandle = self.browser.current_window_handle

    def watchArticle(self, index):
        articleList = self.browser.find_elements_by_class_name(
            'text-link-item-title')
        articleList[index].click()

        self.browser.switch_to.window(self.browser.window_handles[1])
        if self.browser.title == '内容详情':
            self.browser.refresh()
            time.sleep(5)
        print('开始文章：' + self.browser.title)
        start = time.time()
        self.browser.execute_script('window.scrollTo(0, window.innerHeight)')
        for i in range(70):
            key = Keys.DOWN
            if random.random() > 0.5:
                key = Keys.UP
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
        logoDom = self.browser.find_elements_by_class_name('radio-inline')[0]
        logoDom.click()
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])
        self.videoListHandle = self.browser.current_window_handle
        time.sleep(2)
        # self.browser.find_element_by_link_text('学习专题报道').click()
        self.browser.find_elements_by_class_name('tab-wrapper')[11].click()
        time.sleep(2)
        self.browser.find_element_by_class_name('list').click()

    def watchVideo(self, index):
        videoList = self.browser.find_elements_by_class_name(
            'text-link-item-title')
        videoList[index].click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        # self.browser.execute_script('window.scrollTo(0, window.innerHeight)')
        if(self.browser.title == '视频播放'):
            print('刷新试试↓↓↓')
            self.browser.refresh()
            # self.browser.execute_script('window.scrollTo(0, window.innerHeight)')
            time.sleep(3)
            self.browser.find_element_by_class_name('outter').click()
        print('开始视频：' + self.browser.title)
        start = time.time()
        time.sleep(2)
        self.browser.execute_script(
            'document.getElementsByClassName("prism-controlbar")[0].style.display="block"')
        time.sleep(4)
        # try:
        #     totalTime = self.browser.find_element_by_class_name(
        #         'duration').text
        #     _totalTime = int(totalTime.split(
        #         ':')[0]) * 60 + int(totalTime.split(':')[1])
        # except:
        #     _totalTime = 180
        # if _totalTime > 200:
        #     _totalTime = 200
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

        # self.browser.find_element_by_class_name('prism-play-btn').click()
        # self.browser.execute_script('document.getElementsByClassName("prism-play-btn")[0].click()')

        # for i in range(_totalTime):
        #     key = Keys.DOWN
        #     if random.random() > 0.5:
        #         key = Keys.UP
        #     ActionChains(self.browser).key_down(key).perform()
        #     time.sleep(1)
        # self.browser.execute_script('window.scrollTo(0, 0)')

        # ActionChains(self.browser).move_by_offset(0, 0).move_by_offset(1100, 1045).click().perform()
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
        return r

username = input('输入钉钉账号: ')
pwd = input('输入钉钉密码: ')
myTechnologyPower = TechnologyPower(username, pwd)
