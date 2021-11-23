import requests
from os.path import dirname, abspath, exists
from json import load


def main():
    url = 'http://www.pushplus.plus/send'
    with open("/data/config.json" if exists("/data/config.json") else f'{dirname(abspath(__file__))}/config.json', 'r', encoding='utf-8') as user_file:
        user_data = load(user_file)
    for user in user_data:
        if len(user['_token']) > 10:
            name = user['_name']
            content = ""
            data = {'token': user['_token'], 'title': "标题", 'content': content, 'template': "txt"}
            print(name, requests.post(url, data=data).json())
        

if __name__ == '__main__':
    main()
    