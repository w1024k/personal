# coding=utf-8
import itchat, gevent, Queue, time
from threading import Thread


class Wechat(object):
    def __init__(self):
        try:
            itchat.auto_login(hotReload=True)
        except:
            print '登陆失败，请检查你的网络！'
        self.friend_list = []
        self.rooms = []

    def get_friends(self, update=False):
        self.friend_list = []
        for friend in itchat.get_friends(update=update):
            detail = {
                'nickname': friend['NickName'],
                'signature': friend['Signature'],
                'sex': friend['Sex']
            }
            print '昵称：%s 性别:%s\n 签名：%s' % (detail['nickname'].encode('utf-8'), detail['sex'], detail['signature'].encode('utf-8'))
            self.friend_list.append(detail)

    def get_profile(self):
        if not self.friend_list:
            self.get_friends()
        profile = self.friend_list[0]
        print '昵称：%s 性别:%s\n 签名：%s' % (profile['nickname'].encode('utf-8'), profile['sex'], profile[
            'signature'].encode('utf-8'))
        return profile

    def get_rooms(self, update=False):
        """
        需要保存到通讯录中
        :param update:
        :return:
        """
        self.rooms = []
        for room in itchat.get_chatrooms(update=update):
            detail = {
                'nickname': room['NickName'],
                'memberCount': room['MemberCount'],
            }
            print '群昵称:%s    成员数量:%s' % detail['nickname'].encode('utf-8'), detail['memberCount']
            self.rooms.append(detail)

    def send_friend(self, times=1, name='', msg='', wait_time=0, split_time=1):
        name = name.decode('utf-8')
        user = itchat.search_friends(name=name) or itchat.search_chatrooms(name=name)
        username = user[0]['UserName'] if user else None

        if wait_time:
            thread = Thread(target=self.send_friend_handler,
                            args=(times, msg, username, split_time, wait_time))

            thread.start()
            print '%s秒后会将消息送达！！' % wait_time
        else:
            itchat.send(msg=msg, toUserName=username)

    def send_friend_handler(self, times, msg, toUsername, split_time, wait_time):
        time.sleep(wait_time)
        for _ in range(times):
            itchat.send(msg=msg, toUserName=toUsername)
            time.sleep(split_time)

    def sex_count(self):
        if not self.friend_list:
            self.get_friends(update=True)
        man = woman = other = 0
        for friend in self.friend_list:
            if friend['sex'] == 1:
                man += 1
            elif friend['sex'] == 0:
                woman += 1
            else:
                other += 1
        print '男：%s\n 女: %s\n 其他: %s' % (man, woman, other)

    def send_all_handler(self, q, msg):
        if not q.empty():
            name = q.get()
            itchat.send(toUserName=name, msg=msg)

    def send_all(self, msg):
        q = Queue.Queue()
        if not self.friend_list:
            self.get_friends(update=True)
        for friend in self.friend_list:
            q.put(friend["UserName"])
        gevent.joinall([gevent.spawn(self.send_all_handler) for _ in range(len(self.friend_list))])


if __name__ == '__main__':
    wechat = Wechat()
    #print wechat.get_friends()
    #print wechat.sex_count()
    wechat.send_friend(times=6, name='园林', msg='hello world', wait_time=60, split_time=5)
