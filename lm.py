# coding=utf-8
import requests, urllib
import ujson as json

login_url = "http://120.27.18.252:5678/rest/user/login"

profile ={"data":json.dumps({"email": "amanda", "password": "888888", "remember": False})}

headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            }

session = requests.session()
session.post(url=login_url, data=profile, headers=headers)


url = "http://120.27.18.252:5678/rest/candidate/list"
params = {
            "byfilter": "-8889",
                "ordering": "-lastUpdateDate",
                    "paginate_by": 10,
                        "page": 1,
                        }

rsp = session.get(url=url, data=params, headers=headers)
print rsp

