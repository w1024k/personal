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
                                                                    picDir=self.pic, qrCallback=self.callback)))

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
