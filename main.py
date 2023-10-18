import requests
import json
import datetime
import time
from bs4 import BeautifulSoup


# from zhdate import ZhDate


class SendMessage():  # 定义发送消息的类
    def __init__(self):
        self.id = 'wx6d771010554cda6d'
        self.secret = '79b26ff445c5e855bb4b67e30f3d1264'
        self.url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.id}&secret={self.secret}'
        self.access_token = ''
        self.get_access_token()
        self.get_users_openid_url = f'https://api.weixin.qq.com/cgi-bin/user/get?access_token={self.access_token}&next_openid='
        self.send_url = f'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={self.access_token}'
        self.users_id = []

    def get_access_token(self):
        resp = requests.get(self.url, )
        self.access_token = resp.json()['access_token']
        print(resp.text)

    def get_users_openid(self):
        resp = requests.get(self.get_users_openid_url)
        print(resp.text)
        self.users_id = resp.json()['data']['openid']

    def send_msg_to_users(self):
        data = {
            "touser": "oH4rR6k2zT-sCGFmUzTYIYC4ozGI",
            "template_id": "J5WOLMzBwV6TDCKnZETuxezVDwTGcLQqjbw9ZP4ABb8",
            "url": "",
            "topcolor": "#FF0000",
            "data": {
                "HEAD": {
                    "value": "瓜婆娘",
                    "color": "#FF99CC"
                },
                "BODY": {
                    "value": "狗东西",
                    "color": "#EA0000"
                },
                "LAST": {
                    "value": "龟儿子",
                    "color": "#00EC00"
                }
                # "Date": {
                #     "value": "06月07日 19时24分",
                #     "color": "#173177"
                # },
                # "CardNumber": {
                #     "value": "0426",
                #     "color": "#173177"
                # },
                # "Type": {
                #     "value": "消费",
                #     "color": "#173177"
                # },
                # "Money": {
                #     "value": "人民币260.00元",
                #     "color": "#173177"
                # },
                # "DeadTime": {
                #     "value": "06月07日19时24分",
                #     "color": "#173177"
                # },
                # "Left": {
                #     "value": "6504.09",
                #     "color": "#173177"
                # }

            }

        }

        # for user_id in self.users_id:
        #     pass
        data = bytes(json.dumps(data,ensure_ascii=False).encode('utf-8'))
        resp= requests.post(self.send_url,data=data)
        print(resp.text)

if __name__ == '__main__':
    sends = SendMessage()
    # sends.get_access_token()
    sends.get_users_openid()
    sends.send_msg_to_users()
