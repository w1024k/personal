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



def sync_task(run, **kwargs):
    while True:
        command = yield
        threading.Thread(target=run, kwargs=kwargs).start()
        print '%s start' % command


def send_friend_handler(self, times, msg, toUsername, split_time, wait_time):
    sleep(wait_time)
    for _ in range(times):
        itchat.send(msg=msg, toUserName=toUsername)
        sleep(split_time)


def send_all_handler(username, msg):
    itchat.send(toUserName=username, msg=msg)
