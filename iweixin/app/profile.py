# coding:utf-8
import itchat, os
from utils import tools
from . import BaseHandler
from tornado import gen
import time


class Test(BaseHandler):
    def get(self, *args, **kwargs):
        self.write('ok')


class Login(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        no = tools.create_uuid()
        record = os.path.join(os.path.dirname(__file__), 'record')
        pkl = os.path.join(record, no)
        pic = os.path.join(record, '%s.jpg' % no)
        yield itchat.auto_login(hotReload=True, statusStorageDir=pkl,
                          picDir=pic)
        print 1111
        while True:
            print 222
            if os.path.exists(pic):
                f = open(pic, 'rb')
                self.write(f.read())
                self.set_header("Content-type", "image/png")
            else:
                time.sleep(1)
