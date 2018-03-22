import copy
import threading
import itchat
from flask import Flask, request, Response
import ujson as json
from weixin.settings import *

app = Flask(__name__)


@app.route('/')
def test():
    return 'Hello world'


@app.route('/friends/')
def friend_list():
    rsp_data = copy.copy(ERROR['SUCC'])
    try:
        friend_list = itchat.get_friends(request.args.get('update', False))
    except Exception as e:
        rsp_data = copy.copy(ERROR['ERROR'])
        rsp_data['data'] = e
        return Response(json.dumps(rsp_data), mimetype='application/json')
    records = list()
    for friend in friend_list:
        detail = {
            u'昵称': friend['NickName'],
            u'签名': friend['Signature'],
            u'性别': SEX_CHOICES[friend['Sex']],
        }
        records.append(detail)
    rsp_data['data'] = records
    return Response(json.dumps(rsp_data), mimetype='application/json')





if __name__ == '__main__':
    t = threading.Thread(target=itchat.auto_login, kwargs=(dict(hotReload=True, loginCallback=loginCallback)))
    t.start()
    print 'http://127.0.0.1:8000'
    app.run(host='127.0.0.1', port=8000, debug=True)
