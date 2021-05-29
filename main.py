import requests, json, time, sys
from lxml import etree

def Epidemic(i, _name, _username, _password, _useragent, _notify, _token):
    n = i + 1
    url = 'http://xg.kmmu.edu.cn/SPCP/Web/'
    session = requests.session()
#     user_agent = _useragent
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': _useragent
    }
    resp = session.get(url=url, headers=headers)
    tree = etree.HTML(resp.text)
    reSubmiteFlag = tree.xpath('//*[@id="form1"]/input[1]/@value')[0]
#     txtUid = _username
#     txtPwd = _password
    # 封装post请求数据
    post_data = {
        'ReSubmiteFlag': reSubmiteFlag,
        'txtUid': _username,
        'txtPwd': _password,
        'StuLoginMode': 1,
        'codeInput': ''
    }
    resp = session.post(url=url, data=post_data, headers=headers)
    tree = etree.HTML(resp.text)
    result = str(tree.xpath('/html/body/script/text()'))
    if result.find('用户名或者密码错误，请重新输入!') != -1:
        print(f'{get_time()} {_name}用户名或者密码错误!')
        content = {
            "原因": "用户名或者密码错误!",
            "读取的账号": _username,
            "读取的密码": _password,
            }
        pushPlusNotify(_notify, _token, '登陆失败！', json.dumps(content), 'json')
        tgNotify_msg = f'{_name}\n\t\t└登陆失败！\n'
    else:
        # 进入签到页面的URL
        indexUrl = 'http://xg.kmmu.edu.cn/SPCP/Web/Report/Index'
        resp = session.get(url=indexUrl, headers=headers)
        tree = etree.HTML(resp.text)
        result = str(tree.xpath('/html/body/script/text()'))
        if result.find('当前采集日期已登记！') != -1:
            print(f'{get_time()} {_name}当前采集日期已登记！')
            tgNotify_msg = ''
        elif result.find('只能1点至18点可以填报！') != -1:
            tgNotify_msg = f'账号{n}：{_name}\n\t\t└只能1点至18点可以填报！'
            print(f'{get_time()} {_name}只能1点至18点可以填报！\n')
            # sys.exit()
        elif result.find('填报信息还未配置或开启，不能填报！') != -1:
            tgNotify_msg = f'账号{n}：{_name}\n\t\t└填报信息还未配置或开启！\n'
            print(f'{get_time()} 只能1点至18点可以填报！准备结束进程~')
            errorMsg = f'填报信息还未配置或开启，不能填报！\n原因可能是平台出错，请耐心等待下午的重新签到或自查！\n登录网址：{url}\n签到入口：{url}Account/ChooseSys\n表单网址：{indexUrl}'
            pushPlusNotify(_notify, _token, '签到失败！', errorMsg, 'txt')
        else:
            with open('./PZData.json', 'r', encoding='utf-8') as PZData_file:
                PZData = json.load(PZData_file)
            post_data = {
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
                'PZData': f'{PZData}',
                'ReSubmiteFlag': tree.xpath('//*[@id="SaveBtnDiv"]/input[13]/@value')[0]
            }
            # 发起post请求
            try:
                resp2 = session.post(url=indexUrl, data=post_data, headers=headers)
                if resp2.ok:
                    tree2 = etree.HTML(resp2.text)
                    result2 = str(tree2.xpath('/html/body/script/text()'))
                    if result2.find('提交成功！') != -1:
                        print(f'{get_time()} {_name}签到成功~')
                        tgNotify_msg = f'账号{n}：{_name}\n\t\t└签到成功~\n'
                        if time.localtime()[3] == 7: # 云函数用的是UTC+0
                            # 封装pushplus的post数据包
                            post_data = {
                                "自检步骤": "访问下面的网址，登录并签到，以检查是否签到成功",
                                "登录网址": url,
                                "学号及账号": tree.xpath('//*[@id="StudentId"]/@value')[0],
                                "密码": _password,
                                "姓名": tree.xpath('//*[@id="Name"]/@value')[0],
                                "性别": tree.xpath('//*[@id="Sex"]/@value')[0],
                                "班级": tree.xpath('//*[@id="ClassName"]/@value')[0],
                                "手机号": tree.xpath('//*[@id="MoveTel"]/@value')[0],
                                "当前所在地": tree.xpath('//*[@id="ProvinceName"]/@value')[0] + tree.xpath('//*[@id="CityName"]/@value')[0] + tree.xpath('//*[@id="CountyName"]/@value')[0] + tree.xpath('//*[@id="form1"]/div[1]/div[4]/div[2]/input/@value')[0],
                                "家庭住址": tree.xpath('//*[@id="FaProvinceName"]/@value')[0] + tree.xpath('//*[@id="FaCityName"]/@value')[0] + tree.xpath('//*[@id="FaCountyName"]/@value')[0] + tree.xpath('//*[@id="form1"]/div[1]/div[5]/div[2]/input/@value')[0],
                            }
                            pushPlusNotify(_notify, _token, '今早签到可能失败，请自查！（附签到表单内容）', json.dumps(post_data), 'json')
                            tgNotify_msg = f'账号{n}：{_name}\n\n\t└早上签到失败！已补签且通知检查~\n'
            except:
                print(f'{get_time()} {_name}签到失败！')
                tgNotify_msg = f'账号{n}：{_name}\n\t\t└早上的签到失败！\n'
    return tgNotify_msg

def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

with open('./config.json', 'r', encoding='utf-8') as user_file:
    user_data = json.load(user_file)

with open('./agent.json', 'r', encoding='utf-8') as UA_file:
    UA_data = json.load(UA_file)

def pushPlusNotify(notify, token, title, content, template):
    if notify and str(token).find('XX') == -1:
        url = 'http://www.pushplus.plus/send'
        # 封装pushplus的post数据包
        data = {
            # 在 http://www.pushplus.plus/push1.html 申请token
            'token': token,
            'title': title,
            'content': content,
            'template': template
            }
        # 发起post请求
        requests.post(url=url, data=data)

def tgNofity(start, tgNotify_msg, bot_token, user_id):
    if start and tgNotify_msg != '【易班疫情防控签到】\n\n':
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        data = {
            "chat_id": user_id,
            "text": tgNotify_msg,
            "disable_web_page_preview": False
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        try:
            r = requests.post(url=url, data=data, headers=headers)
            if r.ok:
                print("Telegram发送通知消息成功🎉。\n")
            elif r.status_code == '400':
                print("请主动给bot发送一条消息并检查接收用户ID是否正确。\n")
            elif r.status_code == '401':
                print("Telegram bot token 填写错误。\n")
        except Exception as error:
            print(f"telegram发送通知消息失败！！\n{error}")


def main(event, context):
    try:
        with open('./bot.json', 'r', encoding='utf-8') as bot_file:
            bot_data = json.load(bot_file)
        bot_token = bot_data['bot_token']
        user_id = bot_data['user_id']
        shart = True
    except:
        bot_token = None
        user_id = None
        shart = False

    info = '【易班疫情防控签到】\n\n'
    for i in range(len(user_data)):
        try:
            info = info + Epidemic(i, user_data[i]['_name'], user_data[i]['_username'], user_data[i]['_password'], UA_data[i % len(UA_data)], user_data[i]['_notify'], user_data[i]['_token'])
        except Exception as error:
            tgNofity(shart, str(error), bot_token, user_id)
            continue
    tgNofity(shart, info, bot_token, user_id)


if __name__ == '__main__':
    main("","")
