import json

import requests


def send_single_sms(apikey, code, mobile):
    # 发送单条短信
    url = "url在云片网中的API中找到"
    text = "这是云片网中通过审核的短信模板{0}".format(code)

    res = requests.post(url, data={
        "apikey": apikey,# 在云片网中可以找到,
        "mobile": mobile,
        "text": text
    })
    res_json = json.loads(res.text)
    return res_json


# if __name__ == '__main__':
#     res = send_single_sms("apikey", "123456", "这里是手机号码")
#     import json
#     res_json = json.load(res.text)
#     code = res_json['code']
#     msg = res_json['msg']
#     if code == 0:
#         print("发送成功")
#     else:
#         print("发送失败的原因{0}".format(msg))
#     print(res.text)