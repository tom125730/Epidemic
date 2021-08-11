from lxml import etree
import json
import requests
import time


def epidemic():
    url = 'http://xg.kmmu.edu.cn/SPCP/Web/'
    session = requests.session()
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': agent
    }
    resp = session.get(url=url, headers=headers)
    tree = etree.HTML(resp.text)
    reSubmiteFlag = tree.xpath('//*[@id="form1"]/input[1]/@value')[0]
    data = {
        'ReSubmiteFlag': reSubmiteFlag,
        'txtUid': username,
        'txtPwd': password,
        'StuLoginMode': 1,
        'codeInput': ''
    }
    resp = session.post(url=url, data=data, headers=headers)
    tree = etree.HTML(resp.text)
    result = str(tree.xpath('/html/body/script/text()'))
    if "用户名或者密码错误，请重新输入" in result:
        print(f'{get_time()} {name}用户名或者密码错误!')
        content = {
            "失败原因": "用户名或者密码错误!",
            "读取的账号": username,
            "读取的密码": password,
        }
        push('登陆失败！', json.dumps(content), 'json')
        return
    indexUrl = 'http://xg.kmmu.edu.cn/SPCP/Web/Report/Index'
    resp = session.get(url=indexUrl, headers=headers)
    tree = etree.HTML(resp.text)
    result = str(tree.xpath('/html/body/script/text()'))
    if "当前采集日期已登记！" in result:
        print(f'{get_time()} {name}当前采集日期已登记！')
        return
    elif "只能1点至18点可以填报！" in result:
        print(f'{get_time()} {name}只能1点至18点可以填报！\n')
        return
    elif "填报信息还未配置或开启，不能填报！" in result:
        print(f'{get_time()} 填报信息还未配置或开启，不能填报！！')
        errorMsg = f'填报信息还未配置或开启，不能填报！\n' \
                   f'原因可能是平台出错，请耐心等待下午的重新签到或自查！\n' \
                   f'登录网址：{url}\n' \
                   f'签到入口：{url}Account/ChooseSys\n' \
                   f'表单网址：{url}Report/Index'
        push('签到失败！', errorMsg, 'txt')
        return
    with open('./PZData.json', 'r', encoding='utf-8') as PZData_file:
        PZData = json.load(PZData_file)
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
        'PZData': str(PZData),
        'ReSubmiteFlag': tree.xpath('//*[@id="SaveBtnDiv"]/input[13]/@value')[0]
    }
    resp = session.post(url=indexUrl, data=data, headers=headers)
    if resp.ok:
        print(f'{get_time()} {name}签到成功！')
    if time.localtime()[3] != 7:
        return
    if resp.ok:
        tree = etree.HTML(resp.text)
        if '提交成功！' not in tree.xpath('/html/body/script/text()'):
            return
        post_data = {
            "自检步骤": "访问下面的网址，登录并签到，以检查是否补签成功",
            "登录网址": url,
            "学号": tree.xpath('//*[@id="StudentId"]/@value')[0],
            "密码": password,
            "姓名": tree.xpath('//*[@id="Name"]/@value')[0],
            "性别": tree.xpath('//*[@id="Sex"]/@value')[0],
            "班级": tree.xpath('//*[@id="ClassName"]/@value')[0],
            "手机号": tree.xpath('//*[@id="MoveTel"]/@value')[0],
            "当前所在地": tree.xpath('//*[@id="ProvinceName"]/@value')[0] + tree.xpath('//*[@id="CityName"]/@value')[0] +
                     tree.xpath('//*[@id="CountyName"]/@value')[0] +
                     tree.xpath('//*[@id="form1"]/div[1]/div[4]/div[2]/input/@value')[0],
            "家庭住址": tree.xpath('//*[@id="FaProvinceName"]/@value')[0] + tree.xpath('//*[@id="FaCityName"]/@value')[0] +
                    tree.xpath('//*[@id="FaCountyName"]/@value')[0] +
                    tree.xpath('//*[@id="form1"]/div[1]/div[5]/div[2]/input/@value')[0],
        }
        push('今早签到可能失败，请自查！（附签到表单内容）', json.dumps(post_data), 'json')
    else:
        post_data = {
            "网址": url,
            "学号": username,
            "密码": password,
            "姓名": user
        }
        push('今天未成功签到！', json.dumps(post_data), 'json')


def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def push(title, content, template):
    if notify and "XX" not in token:
        url = 'http://www.pushplus.plus/send'
        data = {
            'token': token,
            'title': title,
            'content': content,
            'template': template
        }
        requests.post(url=url, data=data)


def main(event, context):
    global name, username, password, agent, notify, token
    with open('./config.json', 'r', encoding='utf-8') as user_file:
        user_data = json.load(user_file)
    with open('./agent.json', 'r', encoding='utf-8') as UA_file:
        UA_data = json.load(UA_file)
    for i in range(len(user_data)):
        name = user_data[i]['_name']
        username = user_data[i]['_username']
        password = user_data[i]['_password']
        agent = UA_data[i % len(UA_data)]
        notify = user_data[i]['_notify']
        token = user_data[i]['_token']
        epidemic()


if __name__ == '__main__':
    name, username, password, agent, notify, token = "", "", "", "", "", ""
    main("", "")
