#coding=utf-8

'''
pip install pyftpdlib
'''
import sys
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
#判断是否输入ip
pList = sys.argv
if len(pList)>1:
    ip = pList[1]
else:
    import re,os
    ip = re.search(r'(?P<ip>192.168.*?)\s',os.popen('ifconfig').read()).group('ip')

# 实例化DummyAuthorizer来创建ftp用户

authorizer = DummyAuthorizer()

# 参数：用户名，密码，目录，权限
#authorizer.add_user('user', '12345', '/', perm='elradfmwMT')

# 匿名登录
authorizer.add_anonymous('/',perm='elradfmwMT')
handler = FTPHandler
handler.authorizer = authorizer

# 参数：IP，端口，handler
server = FTPServer(
    (ip, 21),
    handler)
print 'ftp://%s/'%ip
server.serve_forever()
