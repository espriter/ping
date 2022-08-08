import time
from ping3 import ping
import requests as res
import json

def ping_nas():
    ping_list = ["sothojishin.direct.quickconnect.to"]

    # URL 읽기
    f = open("/home/espriter/git/ping/webhook_url.txt", 'r')
    url_read = f.readline()
    f.close()

    try:
        for lst in ping_list:
            result = ping(lst)
            if result == False:
                fail_msg = str('NAS Ping이 실패했어요! → ' + lst)
                headers = {"Content-type": "application/json"}
                data = {"text": fail_msg }
                res_result = res.post(url_read, headers=headers, data=json.dumps(data))
                print(res_result.status_code)

            else:
                success_msg = str('NAS Ping이 성공했어요! → ' + lst)
                headers = {"Content-type": "application/json"}
                data = {"text": success_msg }
                res_result = res.post(url_read, headers=headers, data=json.dumps(data))
                print(res_result.status_code)
            time.sleep(2)
    except Exception as e:
        print("Error Log = ", e)

ping_nas()