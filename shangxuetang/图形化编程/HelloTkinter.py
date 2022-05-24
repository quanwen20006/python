# _*_coding:utf-8 _*_
'''
Tkinter学习
'''
# python发短消息
import time
from twilio.rest import Client


text = "任务1快到期了"
auth_token = "b724243601d0fd510d477d5b5a9a0eb6"
account_sid = "AC1c6c29be5d2e11f7ff4402914463acf0"

client = Client(account_sid, auth_token)


def send_msg(phone):
    mes = client.messages.create(from_="+17208975521", body=text, to=phone)
    print("发送成功")
    return mes


if __name__ == "__main__":
    mes = send_msg("+8618589095823")
    print("发送情况：", mes.sid)
