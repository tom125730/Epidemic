import requests ,json ,time ,sys
from lxml import etree
def Epidemic (O0O0O0O00000OOOOO ,_OOOO0000OO00O0OO0 ,_OO000OOO0O0000O0O ,_O0OOO0OO00O00OOOO ,_O00O0000OOOO00OO0 ,_O0O00O0OO0OO0O000 ,_OOO0O0000OOO00O0O ):
    O0O0OOOO0O0OOOO00 =O0O0O0O00000OOOOO +1
    O0O00OOO0O0OO0OOO ='http://xg.kmmu.edu.cn/SPCP/Web/'
    O0O000000O00000OO =requests .session ()
    OOO0O0O000OO000OO ={'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','user-agent':_O00O0000OOOO00OO0 }
    OOOOO00OO0OO0OO0O =O0O000000O00000OO .get (url =O0O00OOO0O0OO0OOO ,headers =OOO0O0O000OO000OO )
    OO0000OOO00O00000 =etree .HTML (OOOOO00OO0OO0OO0O .text )
    OOOO00000OO0OOOOO =OO0000OOO00O00000 .xpath ('//*[@id="form1"]/input[1]/@value')[0 ]
    OOO0OO0O0O0O0O0O0 ={'ReSubmiteFlag':OOOO00000OO0OOOOO ,'txtUid':_OO000OOO0O0000O0O ,'txtPwd':_O0OOO0OO00O00OOOO ,'StuLoginMode':1 ,'codeInput':''}
    OOOOO00OO0OO0OO0O =O0O000000O00000OO .post (url =O0O00OOO0O0OO0OOO ,data =OOO0OO0O0O0O0O0O0 ,headers =OOO0O0O000OO000OO )
    OO0000OOO00O00000 =etree .HTML (OOOOO00OO0OO0OO0O .text )
    O000OO00O0OOO0O0O =str (OO0000OOO00O00000 .xpath ('/html/body/script/text()'))
    if O000OO00O0OOO0O0O .find ('用户名或者密码错误，请重新输入!')!=-1 :
        print (f'{get_time()} {_OOOO0000OO00O0OO0}用户名或者密码错误!')
        O000OOOO0O0O00OOO ={"原因":"用户名或者密码错误!","读取的账号":_OO000OOO0O0000O0O ,"读取的密码":_O0OOO0OO00O00OOOO ,}
        pushPlusNotify (_O0O00O0OO0OO0O000 ,_OOO0O0000OOO00O0O ,'登陆失败！',json .dumps (O000OOOO0O0O00OOO ),'json')
        OOOO0OOO00O00O0O0 =f'{_OOOO0000OO00O0OO0}\n\t\t└登陆失败！\n'
    else :
        OOO0OO0O0OO0OO0O0 ='http://xg.kmmu.edu.cn/SPCP/Web/Report/Index'
        OOOOO00OO0OO0OO0O =O0O000000O00000OO .get (url =OOO0OO0O0OO0OO0O0 ,headers =OOO0O0O000OO000OO )
        OO0000OOO00O00000 =etree .HTML (OOOOO00OO0OO0OO0O .text )
        O000OO00O0OOO0O0O =str (OO0000OOO00O00000 .xpath ('/html/body/script/text()'))
        if O000OO00O0OOO0O0O .find ('当前采集日期已登记！')!=-1 :
            print (f'{get_time()} {_OOOO0000OO00O0OO0}当前采集日期已登记！')
            OOOO0OOO00O00O0O0 =''
        elif O000OO00O0OOO0O0O .find ('只能1点至18点可以填报！')!=-1 :
            OOOO0OOO00O00O0O0 =f'账号{O0O0OOOO0O0OOOO00}：{_OOOO0000OO00O0OO0}\n\t\t└只能1点至18点可以填报！'
            print (f'{get_time()} {_OOOO0000OO00O0OO0}只能1点至18点可以填报！\n')
        elif O000OO00O0OOO0O0O .find ('填报信息还未配置或开启，不能填报！')!=-1 :
            OOOO0OOO00O00O0O0 =f'账号{O0O0OOOO0O0OOOO00}：{_OOOO0000OO00O0OO0}\n\t\t└填报信息还未配置或开启！\n'
            print (f'{get_time()} 只能1点至18点可以填报！准备结束进程~')
            O0OOO0OO0OO0O000O =f'填报信息还未配置或开启，不能填报！\n原因可能是平台出错，请耐心等待下午的重新签到或自查！\n登录网址：{O0O00OOO0O0OO0OOO}\n签到入口：{url}Account/ChooseSys\n表单网址：{OOO0OO0O0OO0OO0O0}'
            pushPlusNotify (_O0O00O0OO0OO0O000 ,_OOO0O0000OOO00O0O ,'签到失败！',O0OOO0OO0OO0O000O ,'txt')
        else :
            with open ('./PZData.json','r',encoding ='utf-8')as OO000O00000OOO000 :
                O0O0O00OO00O0OO0O =json .load (OO000O00000OOO000 )
            OOO0OO0O0O0O0O0O0 ={'StudentId':OO0000OOO00O00000 .xpath ('//*[@id="StudentId"]/@value')[0 ],'Name':OO0000OOO00O00000 .xpath ('//*[@id="Name"]/@value')[0 ],'Sex':OO0000OOO00O00000 .xpath ('//*[@id="Sex"]/@value')[0 ],'SpeType':OO0000OOO00O00000 .xpath ('//*[@id="SpeType"]/@value')[0 ],'CollegeNo':OO0000OOO00O00000 .xpath ('//*[@id="CollegeNo"]/@value')[0 ],'SpeGrade':OO0000OOO00O00000 .xpath ('//*[@id="SpeGrade"]/@value')[0 ],'SpecialtyName':OO0000OOO00O00000 .xpath ('//*[@id="SpecialtyName"]/@value')[0 ],'ClassName':OO0000OOO00O00000 .xpath ('//*[@id="ClassName"]/@value')[0 ],'MoveTel':OO0000OOO00O00000 .xpath ('//*[@id="MoveTel"]/@value')[0 ],'Province':str (OO0000OOO00O00000 .xpath ('//*[@id="form1"]/div[1]/div[4]/div[2]/select[2]/@data-defaultvalue'))[2 :4 ]+'0000','City':OO0000OOO00O00000 .xpath ('//*[@id="form1"]/div[1]/div[4]/div[2]/select[2]/@data-defaultvalue')[0 ],'County':OO0000OOO00O00000 .xpath ('//*[@id="form1"]/div[1]/div[4]/div[2]/select[3]/@data-defaultvalue')[0 ],'ComeWhere':OO0000OOO00O00000 .xpath ('//*[@id="form1"]/div[1]/div[4]/div[2]/input/@value')[0 ],'FaProvince':str (OO0000OOO00O00000 .xpath ('//*[@id="form1"]/div[1]/div[5]/div[2]/select[2]/@data-defaultvalue'))[2 :4 ]+'0000','FaCity':OO0000OOO00O00000 .xpath ('//*[@id="form1"]/div[1]/div[5]/div[2]/select[2]/@data-defaultvalue')[0 ],'FaCounty':OO0000OOO00O00000 .xpath ('//*[@id="form1"]/div[1]/div[5]/div[2]/select[3]/@data-defaultvalue')[0 ],'FaComeWhere':OO0000OOO00O00000 .xpath ('//*[@id="form1"]/div[1]/div[5]/div[2]/input/@value')[0 ],'radio_1':'71a16876-3d52-4510-8c96-09b232a0161b','radio_2':'083d90f5-5fa2-4a6d-a231-fe315b5104a3','radio_3':'994c60eb-6f68-48bd-8bda-49a8a7ea812c','text_1':'','radio_4':'18e9be47-deee-4eb0-8318-935f7ec832fd','radio_5':'8dce119f-8eba-45b7-ac3c-ecb49e480dd3','radio_6':'fe8b77d7-0014-49e1-bea0-46b0bff13898','Other':'','GetAreaUrl':'/SPCP/Web/Report/GetArea','IdCard':OO0000OOO00O00000 .xpath ('//*[@id="IdCard"]/@value')[0 ],'ProvinceName':OO0000OOO00O00000 .xpath ('//*[@id="ProvinceName"]/@value')[0 ],'CityName':OO0000OOO00O00000 .xpath ('//*[@id="CityName"]/@value')[0 ],'CountyName':OO0000OOO00O00000 .xpath ('//*[@id="CountyName"]/@value')[0 ],'FaProvinceName':OO0000OOO00O00000 .xpath ('//*[@id="FaProvinceName"]/@value')[0 ],'FaCityName':OO0000OOO00O00000 .xpath ('//*[@id="FaCityName"]/@value')[0 ],'FaCountyName':OO0000OOO00O00000 .xpath ('//*[@id="FaCountyName"]/@value')[0 ],'radioCount':'6','checkboxCount':'0','blackCount':'1','PZData':f'{O0O0O00OO00O0OO0O}','ReSubmiteFlag':OO0000OOO00O00000 .xpath ('//*[@id="SaveBtnDiv"]/input[13]/@value')[0 ]}
            try :
                OOOOOOOO0OO0OO00O =O0O000000O00000OO .post (url =OOO0OO0O0OO0OO0O0 ,data =OOO0OO0O0O0O0O0O0 ,headers =OOO0O0O000OO000OO )
                if OOOOOOOO0OO0OO00O .ok :
                    OOOO00O0OO00O0O0O =etree .HTML (OOOOOOOO0OO0OO00O .text )
                    O00OO00OOOO000O0O =str (OOOO00O0OO00O0O0O .xpath ('/html/body/script/text()'))
                    if O00OO00OOOO000O0O .find ('提交成功！')!=-1 :
                        print (f'{get_time()} {_OOOO0000OO00O0OO0}签到成功~')
                        OOOO0OOO00O00O0O0 =f'账号{O0O0OOOO0O0OOOO00}：{_OOOO0000OO00O0OO0}\n\t\t└签到成功~\n'
                        if time .localtime ()[3 ]==7 :
                            OOO0OO0O0O0O0O0O0 ={"自检步骤":"访问下面的网址，登录并签到，以检查是否签到成功","登录网址":O0O00OOO0O0OO0OOO ,"学号及账号":OO0000OOO00O00000 .xpath ('//*[@id="StudentId"]/@value')[0 ],"密码":_O0OOO0OO00O00OOOO ,"姓名":OO0000OOO00O00000 .xpath ('//*[@id="Name"]/@value')[0 ],"性别":OO0000OOO00O00000 .xpath ('//*[@id="Sex"]/@value')[0 ],"班级":OO0000OOO00O00000 .xpath ('//*[@id="ClassName"]/@value')[0 ],"手机号":OO0000OOO00O00000 .xpath ('//*[@id="MoveTel"]/@value')[0 ],"当前所在地":OO0000OOO00O00000 .xpath ('//*[@id="ProvinceName"]/@value')[0 ]+OO0000OOO00O00000 .xpath ('//*[@id="CityName"]/@value')[0 ]+OO0000OOO00O00000 .xpath ('//*[@id="CountyName"]/@value')[0 ]+OO0000OOO00O00000 .xpath ('//*[@id="form1"]/div[1]/div[4]/div[2]/input/@value')[0 ],"家庭住址":OO0000OOO00O00000 .xpath ('//*[@id="FaProvinceName"]/@value')[0 ]+OO0000OOO00O00000 .xpath ('//*[@id="FaCityName"]/@value')[0 ]+OO0000OOO00O00000 .xpath ('//*[@id="FaCountyName"]/@value')[0 ]+OO0000OOO00O00000 .xpath ('//*[@id="form1"]/div[1]/div[5]/div[2]/input/@value')[0 ],}
                            pushPlusNotify (_O0O00O0OO0OO0O000 ,_OOO0O0000OOO00O0O ,'今早签到可能失败，请自查！（附签到表单内容）',json .dumps (OOO0OO0O0O0O0O0O0 ),'json')
                            OOOO0OOO00O00O0O0 =f'账号{O0O0OOOO0O0OOOO00}：{_OOOO0000OO00O0OO0}\n\n\t└早上签到失败！已补签且通知检查~\n'
            except :
                print (f'{get_time()} {_OOOO0000OO00O0OO0}签到失败！')
                OOOO0OOO00O00O0O0 =f'账号{O0O0OOOO0O0OOOO00}：{_OOOO0000OO00O0OO0}\n\t\t└早上的签到失败！\n'
    return OOOO0OOO00O00O0O0
def get_time ():
    return time .strftime ("%Y-%m-%d %H:%M:%S",time .localtime ())
with open ('./config.json','r',encoding ='utf-8')as user_file :
    user_data =json .load (user_file )
with open ('./agent.json','r',encoding ='utf-8')as UA_file :
    UA_data =json .load (UA_file )
def pushPlusNotify (OOOOOO00O00O00O0O ,OO000000OOO00OO0O ,O000O00OOO0OO0OO0 ,OO0OOOOOO00OOOO0O ,OOOO0O0OO00000OOO ):
    if OOOOOO00O00O00O0O and str (OO000000OOO00OO0O ).find ('XX')==-1 :
        O00OO0O00OO0OO000 ='http://www.pushplus.plus/send'
        OO0OOOO00OO00OO00 ={'token':OO000000OOO00OO0O ,'title':O000O00OOO0OO0OO0 ,'content':OO0OOOOOO00OOOO0O ,'template':OOOO0O0OO00000OOO }
        requests .post (url =O00OO0O00OO0OO000 ,data =OO0OOOO00OO00OO00 )
def tgNofity (OO00OOOO00000O000 ,O0O00OOO000O00000 ,O0O00O0OOO0O000OO ,OOOOOO0O0O0OO0O00 ):
    if OO00OOOO00000O000 and O0O00OOO000O00000 !='【易班疫情防控签到】\n\n':
        O0OO0O0O00000OO00 =f'https://api.telegram.org/bot{O0O00O0OOO0O000OO}/sendMessage'
        OO0OOO0OO0O00O00O ={"chat_id":OOOOOO0O0O0OO0O00 ,"text":O0O00OOO000O00000 ,"disable_web_page_preview":False }
        OO00OOOO00000000O ={'Content-Type':'application/x-www-form-urlencoded'}
        try :
            O0O000O0O000OOO00 =requests .post (url =O0OO0O0O00000OO00 ,data =OO0OOO0OO0O00O00O ,headers =OO00OOOO00000000O )
            if O0O000O0O000OOO00 .ok :
                print ("Telegram发送通知消息成功🎉。\n")
            elif O0O000O0O000OOO00 .status_code =='400':
                print ("请主动给bot发送一条消息并检查接收用户ID是否正确。\n")
            elif O0O000O0O000OOO00 .status_code =='401':
                print ("Telegram bot token 填写错误。\n")
        except Exception as OOO0O000O0O0O0O0O :
            print (f"telegram发送通知消息失败！！\n{OOO0O000O0O0O0O0O}")
def main (O0OOOOOO0O0O00OO0 ,O0OOO0000OO0O0OO0 ):
    try :
        with open ('./bot.json','r',encoding ='utf-8')as O0O000OOOO0O000OO :
            O0OOO0OOO00OO00OO =json .load (O0O000OOOO0O000OO )
        OOO00OOOO00O00O0O =O0OOO0OOO00OO00OO ['bot_token']
        O0O0O00OOOO000000 =O0OOO0OOO00OO00OO ['user_id']
        O00OO0O00O0O00O0O =True
    except :
        OOO00OOOO00O00O0O =None
        O0O0O00OOOO000000 =None
        O00OO0O00O0O00O0O =False
    O0O0OOO0O0OO0OOOO ='【易班疫情防控签到】\n\n'
    for O00O00OO000O000O0 in range (len (user_data )):
        try :
            O0O0OOO0O0OO0OOOO =O0O0OOO0O0OO0OOOO +Epidemic (O00O00OO000O000O0 ,user_data [O00O00OO000O000O0 ]['_name'],user_data [O00O00OO000O000O0 ]['_username'],user_data [O00O00OO000O000O0 ]['_password'],UA_data [O00O00OO000O000O0 %len (UA_data )],user_data [O00O00OO000O000O0 ]['_notify'],user_data [O00O00OO000O000O0 ]['_token'])
        except Exception as OOOOOOOOO00O0OO00 :
            tgNofity (O00OO0O00O0O00O0O ,str (OOOOOOOOO00O0OO00 ),OOO00OOOO00O00O0O ,O0O0O00OOOO000000 )
            continue
    tgNofity (O00OO0O00O0O00O0O ,O0O0OOO0O0OO0OOOO ,OOO00OOOO00O00O0O ,O0O0O00OOOO000000 )
if __name__ =='__main__':
    main ("","")
