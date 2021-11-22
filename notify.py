import requests
from os.path import dirname, abspath, exists
from json import load


def push(title, content, template):
    if notify and "XX" not in token:
        url = 'http://www.pushplus.plus/send'
        data = {'token': token, 'title': title, 'content': content, 'template': template}
        print(requests.post(url, data=data).json())
        

def main():
    global notify, token
    with open("/data/config.json" if exists("/data/config.json") else f'{dirname(abspath(__file__))}/config.json', 'r', encoding='utf-8') as user_file:
        user_data = load(user_file)
    for user in user_data:
        token = user['_token']
        content = ""
        push("今日签到情况说明", content, "txt")
        

if __name__ == '__main__':
    notify, token = "", ""
    main()
    