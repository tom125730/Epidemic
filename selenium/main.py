#!usr/bin/python3
# coding: utf-8

from datetime import datetime
from json import load, dumps
from os.path import dirname, abspath
from time import localtime, strftime

from requests import post
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located as located
from selenium.webdriver.support.ui import WebDriverWait as wait


class DailyReport(object):
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('blink-settings=imagesEnabled=false')
        self.options.add_argument('--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 yiban_iOS/4.9.3"')
        self.client = webdriver.Chrome(options=self.options)
        self.index_url = "https://xg.kmmu.edu.cn/SPCP/Web/"
        self.account_url = "https://xg.kmmu.edu.cn/SPCP/Web/Account/ChooseSys"
        self.report_url = "https://xg.kmmu.edu.cn/SPCP/Web/Report/Index"
        self.path = dirname(abspath(__file__))
        with open(f'{self.path}/config.json', 'r', encoding='utf-8') as f1:
            self.data = load(f1)

    def element(self, string, *text):
        ele = wait(self.client, 10, 0.5).until(located((by.XPATH, string))) if "/" in string else wait(self.client, 10, 0.5).until(located((by.ID, string)))
        self.client.execute_script("arguments[0].scrollIntoView();", ele)
        ele.click()
        if text:
            ele.send_keys(text)
        else:
            return ele

    def login(self, _username, _password, _name):
        submit = self.element('Submit')
        self.element("StudentId", _username)
        self.element("Name", _password)
        submit.click()
        try:
            self.client.get(self.report_url)
            self.client.execute_script("var q=document.documentElement.scrollTop=10000")
            self.client.find_element_by_id("18e9be47-deee-4eb0-8318-935f7ec832fd").click()
            self.client.find_element_by_id("8dce119f-8eba-45b7-ac3c-ecb49e480dd3").click()
            self.client.find_element_by_id("fe8b77d7-0014-49e1-bea0-46b0bff13898").click()
            self.client.find_element_by_id("ckCLS").send_keys(Keys.SPACE)
            self.client.find_element_by_class_name("save_form").click()
            print(f'{self.get_time()} {_name} 今日签到成功')
        except NoSuchElementException:
            alart = self.client.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
            if "登录" in alart:
                print(f'{self.get_time()} {_name} 学号或者密码错误')
            elif "登记" in alart:
                print(f'{self.get_time()} {_name} 当前日期已登记')
            else:
                print(f'{self.get_time()} {_name} 无法签到')
        except Exception as error:
            print(f'{self.get_time()} {_name} 发生未知错误 {error}')
        finally:
            loop = True
            while loop:
                try:
                    self.client.get(self.account_url)
                    self.element('//*[@id="cd-nav"]/a')
                    self.element('//*[@id="cd-main-nav"]/ul/li[2]/a')
                    loop = False
                except ElementNotInteractableException:
                    loop = True

    def run(self):
        try:
            self.client.get(self.index_url)
            print("*" * 45)
            for i in range(len(self.data)):
                name = self.data[i]['_name']
                username = self.data[i]['_username']
                password = self.data[i]['_password']
                self.login(username, password, name)
            self.client.close()
            self.client.quit()
            print("*" * 45)
        except Exception as error:
            print(error)
            url = 'http://www.pushplus.plus/send'
            data = {
                "token": self.data[0]['_token'],
                "title": "易班疫情防控签到",
                "content": "发生严重错误无法签到！",
                "template": "txt"
            }
            body = dumps(data).encode(encoding='utf-8')
            headers = {'Content-Type': 'application/json'}
            post(url, data=body, headers=headers)

    @staticmethod
    def get_time():
        return strftime("%m-%d %H:%M:%S", localtime())


if __name__ == '__main__':
    now = datetime.now()
    obj = DailyReport()
    obj.run()
    print('\n运行耗时：', datetime.now() - now)
