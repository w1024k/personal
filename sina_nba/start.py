# coding=utf-8

from score import Score

# from live import Live

s = Score()
s.run('start')


def start():
    print '1:score, 2:live'
    num = raw_input('please choose number') or 1

    try:
        num = int(num)
        if num not in [1, 2]:
            num = 1
        return num
    except:
        start()


num = start()

if num == 1:
    s.run()
else:
    live_num = s.get_rooms()
    print live_num
