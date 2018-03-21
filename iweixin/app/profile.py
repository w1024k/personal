# coding:utf-8
import itchat, os
from utils import tools
from . import BaseHandler
from tornado import gen
import time
import threading


class Test(BaseHandler):
    def get(self, *args, **kwargs):
        self.write('ok')


class Login(BaseHandler):
    def get(self, *args, **kwargs):
        no = tools.create_uuid()
        record = os.path.join(os.path.dirname(__file__), 'record')
        pkl = os.path.join(record, no)
        self.pic = os.path.join(record, '%s.jpg' % no)
        t = threading.Thread(target=itchat.auto_login, kwargs=(dict(hotReload=True, statusStorageDir=pkl,
                                                                    picDir=self.pic, qrCallback=self.callback,
                                                                    loginCallback=self.loginCallback)))

        t.setDaemon(True)
        t.start()
        time_wait = 0.5
        while True:
            if os.path.exists(self.pic):
                break
            elif time_wait > 2:
                self.write('timeout')
                break
            time.sleep(time_wait)
            time_wait += 0.5
        f = open(self.pic, 'rb')
        self.write(f.read())
        self.set_header("Content-type", "image/png")

    def callback(self, uuid, status, qrcode):
        print 'call callback'
        with open(self.pic, 'wb') as f:
            f.write(qrcode)

    def loginCallback(self):
        print 'webbrowser'
        import webbrowser
        webbrowser.open("http://127.0.0.1:8888/get/friends/")


class GetFriends(BaseHandler):
    def get(self):
        html = "<h2>好友列表</h2>"
        for friend in itchat.get_friends(update=True):
            detail = {
                'nickname': friend['NickName'],
                'signature': friend['Signature'],
                'sex': friend['Sex']
            }
            html += '<h3>昵称：%s 性别:%s <br/> 签名：%s</h3><br/>' % (
                detail['nickname'].encode('utf-8'), detail['sex'], detail['signature'].encode('utf-8'))
        self.write(html)
