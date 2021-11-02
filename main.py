import requests
from uuid import uuid4
from os.path import dirname, abspath
from lxml.etree import HTML as html
from json import load, dumps
from time import strftime, localtime
from datetime import datetime


def epidemic():
    session = requests.session()
    url = "https://xg.kmmu.edu.cn/SPCP/Web/"
    headers = {"User-Agent": agent}
    parms = {"ReSubmiteFlag": uuid4(), "StuLoginMode": "1", "txtUid": username, "txtPwd": password, "codeInput": ""}
    resp = session.post(url, data=parms, headers=headers, proxies={"http": None, "https": None})
    alert = str(html(resp.text).xpath('/html/body/script/text()')[0])
    if "用户名或者密码错误" in alert:
        print(f'{get_time()} {name} 用户名或者密码错误!')
        content = {"失败原因": "用户名或者密码错误!", "读取的账号": username, "读取的密码": password}
        push('登陆失败！', dumps(content), 'json')
        return f'{name} 用户名或者密码错误!'
    url = "https://xg.kmmu.edu.cn/SPCP/Web/Report/Index"
    resp = session.get(url, headers=headers, proxies={"http": None, "https": None})
    tree = html(resp.text)
    try:
        alert = str(tree.xpath('/html/body/script/text()')[0])
        if "已登记" in alert:
            print(f'{get_time()} {name} 当前采集日期已登记！')
            return f'{name} 当前采集日期已登记！'
        elif "只能1点至18点" in alert:
            print(f'{get_time()} {name} 只能1点至18点可以填报！')
            return f'{name} 只能1点至18点可以填报！'
        elif "填报信息还未配置或开启" in alert:
            print(f'{get_time()} 填报信息还未配置或开启，不能填报！！')
            error = f'填报信息还未配置或开启，不能填报！\n' \
                    f'原因可能是平台出错，请耐心等待下午的重新签到或自查！\n' \
                    f'登录网址：https://xg.kmmu.edu.cn/SPCP/Web/'
            push('签到失败！', error, 'txt')
            return f"{name} 填报信息还未配置或开启"
    except IndexError:
        data = {
            'StudentId': tree.xpath('//*[@id="StudentId"]/@value')[0],
            'Name': tree.xpath('//*[@id="Name"]/@value')[0],
            'Sex': tree.xpath('//*[@id="Sex"]/@value')[0],
            'SpeType': tree.xpath('//*[@id="SpeType"]/@value')[0],
            'CollegeNo': tree.xpath('//*[@id="CollegeNo"]/@value')[0],
            'SpeGrade': tree.xpath('//*[@id="SpeGrade"]/@value')[0],
            'SpecialtyName': tree.xpath('//*[@id="SpecialtyName"]/@value')[0],
            'ClassName': tree.xpath('//*[@id="ClassName"]/@value')[0],
            'MoveTel': tree.xpath('//*[@id="MoveTel"]/@value')[0],
            'Province': str(tree.xpath('//*[@id="form1"]/div[1]/div[4]/div[2]/select[2]/@data-defaultvalue'))[2:4] + '0000',
            'City': tree.xpath('//*[@id="form1"]/div[1]/div[4]/div[2]/select[2]/@data-defaultvalue')[0],
            'County': tree.xpath('//*[@id="form1"]/div[1]/div[4]/div[2]/select[3]/@data-defaultvalue')[0],
            'ComeWhere': tree.xpath('//*[@id="form1"]/div[1]/div[4]/div[2]/input/@value')[0],
            'FaProvince': str(tree.xpath('//*[@id="form1"]/div[1]/div[5]/div[2]/select[2]/@data-defaultvalue'))[2:4] + '0000',
            'FaCity': tree.xpath('//*[@id="form1"]/div[1]/div[5]/div[2]/select[2]/@data-defaultvalue')[0],
            'FaCounty': tree.xpath('//*[@id="form1"]/div[1]/div[5]/div[2]/select[3]/@data-defaultvalue')[0],
            'FaComeWhere': tree.xpath('//*[@id="form1"]/div[1]/div[5]/div[2]/input/@value')[0],
            'radio_1': '71a16876-3d52-4510-8c96-09b232a0161b',
            'radio_2': '083d90f5-5fa2-4a6d-a231-fe315b5104a3',
            'radio_3': '994c60eb-6f68-48bd-8bda-49a8a7ea812c',
            'text_1': '',
            'radio_4': '18e9be47-deee-4eb0-8318-935f7ec832fd',
            'radio_5': '8dce119f-8eba-45b7-ac3c-ecb49e480dd3',
            'radio_6': 'fe8b77d7-0014-49e1-bea0-46b0bff13898',
            'Other': '',
            'GetAreaUrl': '/SPCP/Web/Report/GetArea',
            'IdCard': tree.xpath('//*[@id="IdCard"]/@value')[0],
            'ProvinceName': tree.xpath('//*[@id="ProvinceName"]/@value')[0],
            'CityName': tree.xpath('//*[@id="CityName"]/@value')[0],
            'CountyName': tree.xpath('//*[@id="CountyName"]/@value')[0],
            'FaProvinceName': tree.xpath('//*[@id="FaProvinceName"]/@value')[0],
            'FaCityName': tree.xpath('//*[@id="FaCityName"]/@value')[0],
            'FaCountyName': tree.xpath('//*[@id="FaCountyName"]/@value')[0],
            'radioCount': '6',
            'checkboxCount': '0',
            'blackCount': '1',
            'PZData': str([
                {"OptionName": "以上症状都没有", "SelectId": "71a16876-3d52-4510-8c96-09b232a0161b", "TitleId": "eb0c8db7-b4dd-4ad6-b58a-626fc3336f16", "OptionType": "0"},
                {"OptionName": "否，身体健康", "SelectId": "083d90f5-5fa2-4a6d-a231-fe315b5104a3", "TitleId": "a9a30b10-f88e-4776-ac74-b5a10fa11886", "OptionType": "0"},
                {"OptionName": "否，不是疑似感染者", "SelectId": "994c60eb-6f68-48bd-8bda-49a8a7ea812c", "TitleId": "37e33b7d-5575-48c3-b59b-d4b7f6a6a0b5", "OptionType": "0"},
                {"OptionName": "否", "SelectId": "18e9be47-deee-4eb0-8318-935f7ec832fd", "TitleId": "986a95ff-5ce4-4417-9810-b1e190594f34", "OptionType": "0"},
                {"OptionName": "否", "SelectId": "8dce119f-8eba-45b7-ac3c-ecb49e480dd3", "TitleId": "3a3a10c8-02a7-4f16-95e5-f8ef5c8bfd75", "OptionType": "0"},
                {"OptionName": "健康", "SelectId": "fe8b77d7-0014-49e1-bea0-46b0bff13898", "TitleId": "6002f891-d80d-4e01-ad6d-651e01df394b", "OptionType": "0"}
            ]),
            'ReSubmiteFlag': uuid4()
        }
        resp = session.post(url, data=data, headers=headers)
        if '提交成功' in resp.text:
            print(f'{get_time()} {name} 签到成功！')
        if localtime()[3] != 7:  # 腾讯云函数的7点是+8时区的15点，23点是+8时区的7点
            return f'{name} 签到成功！'
        if resp.ok and '提交成功' in resp.text:
            post_data = {
                "自检步骤": "访问下面的网址，登录并签到，以检查是否补签成功",
                "登录网址": "https://xg.kmmu.edu.cn/SPCP/Web/",
                "学号": tree.xpath('//*[@id="StudentId"]/@value')[0],
                "密码": password,
                "姓名": tree.xpath('//*[@id="Name"]/@value')[0],
                "班级": tree.xpath('//*[@id="ClassName"]/@value')[0],
                "手机号": tree.xpath('//*[@id="MoveTel"]/@value')[0]
            }
            push('今早签到可能失败，请自查！（附签到表单内容）', dumps(post_data), 'json')
            return f'{name} 今早签到可能失败！'
        else:
            post_data = {"网址": "https://xg.kmmu.edu.cn/SPCP/Web/", "学号": username, "密码": password, "姓名": name}
            push('今天未成功签到！', dumps(post_data), 'json')
            return f'{name} 今天未成功签到！'


def get_time():
    now_time = strftime("%m-%d %H:%M:%S", localtime())
    return now_time


def push(title, content, template):
    if notify and "XX" not in token:
        url = 'http://www.pushplus.plus/send'
        data = {'token': token, 'title': title, 'content': content, 'template': template}
        requests.post(url, data=data)


def main(event, context):
    global name, username, password, agent, notify, token
    now = datetime.now()
    msg = ""
    path = dirname(abspath(__file__))
    with open(f'{path}/config.json', 'r', encoding='utf-8') as user_file:
        user_data = load(user_file)
    with open(f'{path}/agent.json', 'r', encoding='utf-8') as agent_file:
        agent_data = load(agent_file)
    print(f'{get_time()} 总共需要签到的人数：{len(user_data)}\n')
    for user in user_data:
        name = user['_name']
        username = user['_username']
        password = user['_password']
        agent = agent_data[user_data.index(user) % len(agent_data)]
        notify = user['_notify']
        token = user['_token']
        msg += epidemic() + "\n"
    if localtime()[3] == 23:  # 腾讯云函数的7点是+8时区的15点，23点是+8时区的7点
        url = 'http://www.pushplus.plus/send'
        data = {'token': user_data[0]['_token'], 'title': "今日签到情况", 'content': msg, 'template': "txt"}
        requests.post(url, data=data)
    print(f'\n{get_time()} 运行耗时：', datetime.now() - now)


if __name__ == '__main__':
    name, username, password, agent, notify, token = "", "", "", "", "", ""
    main("", "")
