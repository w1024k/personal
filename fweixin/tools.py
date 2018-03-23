# coding:utf-8

from time import ctime, sleep
from socket import *
import webbrowser
import threading
import settings
import itchat
import gevent


def loginCallback():
    webbrowser.open("http://127.0.0.1:8000/")


# @app.task()
# def send_friend_cron(msg, toUsername):
#     itchat.send(msg=msg, toUserName=toUsername)
#     del app.conf['CELERYBEAT_SCHEDULE'][toUsername]



# def sock_server():
#     udpServer = socket(AF_INET, SOCK_DGRAM)
#     udpServer.bind(settings.SOCK_ADDR)
#
#     while True:
#         print('Waiting for connection...')
#         data, addr = udpServer.recvfrom()
#         data = "at %s :%s" % (ctime(), data)
#     udpServer.close()
#
#
# def sock_client(data):
#     udpClient = socket(AF_INET, SOCK_DGRAM)
#     udpClient.sendto(data, settings.SOCK_ADDR)
#     udpClient.close()

def run():
    pass


def sync_task():
    while True:
        command = yield
        threading.Thread(target=run).start()
        print '%s start' % command
