# coding=utf-8
from flask import Flask, request, Response
import copy
import threading
import itchat
import ujson as json
import settings
import tools
import gevent

app = Flask(__name__)


@app.route('/')
def test():
    return 'hello world'


@app.route('/friends/')
def friend_list():
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    try:
        friend_list = itchat.get_friends(request.args.get('update', False))
    except Exception as e:
        rsp_data = copy.copy(settings.ERROR['ERROR'])
        rsp_data['data'] = e
        return Response(json.dumps(rsp_data), mimetype='application/json')
    records = list()
    for friend in friend_list:
        detail = {
            'nickname': friend['NickName'],
            'signature': friend['Signature'],
            'sex': settings.SEX_CHOICES[friend['Sex']],
        }
        records.append(detail)
    rsp_data['data'] = records
    return Response(json.dumps(rsp_data), mimetype='application/json')


@app.route('/profile/')
def chat_room():
    rsp_data = copy.copy(settings.ERROR['SUCC'])

    records = list()
    try:
        chatrooms = itchat.get_chatrooms(request.args.get('update', False))
    except Exception as e:
        rsp_data = copy.copy(settings.ERROR['ERROR'])
        rsp_data['data'] = e
        return Response(json.dumps(rsp_data), mimetype='application/json')
    for room in chatrooms:
        detail = {
            'nickname': room['NickName'],
            'memberCount': room['MemberCount'],
        }
        records.append(detail)
    rsp_data['data'] = records
    return Response(json.dumps(rsp_data), mimetype='application/json')


@app.route('/sex/count/')
def sex_count(self):
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    try:
        friend_list = itchat.get_friends(request.args.get('update', False))
    except Exception as e:
        rsp_data = copy.copy(settings.ERROR['ERROR'])
        rsp_data['data'] = e
        return Response(json.dumps(rsp_data), mimetype='application/json')
    man = woman = other = 0
    for friend in friend_list:
        if friend['sex'] == 1:
            man += 1
        elif friend['sex'] == 0:
            woman += 1
        else:
            other += 1
    rsp_data['data'] = {
        'man': man,
        'woman': woman,
        'other': other,
    }
    return Response(json.dumps(rsp_data), mimetype='application/json')


@app.route('/send/msg/')
def send_friend(times=1, name='', msg='', wait_time=0, split_time=1):
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    times = request.form.get('times', 1)  # 发送次数
    split_time = int(request.form.get('split_time', 1))  # 每次发送间隔时间
    wait_time = request.form.get('wait_time', 0)  # 多少分钟后发送
    name = request.form.get('name', '') and request.form[name].decode('utf-8')  # 昵称

    user = itchat.search_friends(name=name) or itchat.search_chatrooms(name=name)
    if user:
        username = user[0]['UserName']
    else:
        rsp_data = copy.copy(settings.ERROR['NOT_EXIST_USER'])
        return Response(json.dumps(rsp_data), mimetype='application/json')
    params = {
        "times": times,
        "msg": msg,
        "toUsername": username,
        "split_time": split_time,
        "wait_time": wait_time
    }

    tools.sync_task(tools.send_friend_handler, **params)
    return Response(json.dumps(rsp_data), mimetype='application/json')


@app.route('/send/msg/all/')
def send_all():
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    msg = request.form.get('msg', '')
    try:
        friend_list = itchat.get_friends(request.args.get('update', False))
    except Exception as e:
        rsp_data = copy.copy(settings.ERROR['ERROR'])
        rsp_data['data'] = e
        return Response(json.dumps(rsp_data), mimetype='application/json')
    q = list()
    for friend in friend_list:
        q.append(friend["UserName"])
    gevent.joinall([gevent.spawn(tools.send_all_handler, username, msg) for username in friend_list])


if __name__ == '__main__':
    login_thread = threading.Thread(target=itchat.auto_login,
                                    kwargs=(dict(hotReload=True, loginCallback=tools.loginCallback)))
    login_thread.start()
    sync = tools.sync_task()
    next(sync)
    app.run(host='127.0.0.1', port=8000, debug=True)
