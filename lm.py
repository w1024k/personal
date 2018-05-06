# coding=utf-8
import requests, urllib
import ujson as json

login_url = "http://120.27.18.252:5678/rest/user/login"

profile = {"data": json.dumps({"email": "amanda", "password": "888888", "remember": False})}

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
records = rsp.json()
details = list()
for record in records['list']:
    detail = {
        'name': record['chineseName'],
        'company': record['company']['name'],
        'job': record['current']['title'],
        'city': record['city'] and record['city']['name'],
        'salary': record['annualSalary'],
        'age': record['dateOfBirth'],
        'phone': record['mobile'],
        'last_contact': record['lastUpdateDate'],

        'gender': '男' if record['gender'] else '女',
        'school': record['school'],
        'email': record['email'],
        'education': record['education']['value'],
    }
    # print detail
    # details.append(detail)

url = 'http://120.27.18.252:5678/rest/joborder/list?byfilter=-8888&ordering=-lastUpdateDate&page=1&paginate_by=1'

jobs = session.get(url=url).json()

for record in jobs['list']:
    detail = {
        'job_name': record["jobTitle"],
        'company': record['client']['name'],
        'city': record['city'] and record['city']['name'],
        'waiter': [user["user"]["chineseName"] for user in record['users']],
        'worker_count': record['currentCount'],
        'lastupdate': record['lastUpdate'],
    }
    print detail

