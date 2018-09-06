# coding=utf-8
import os
import re
import sys


def kill_process(port):
    process_detail_list = os.popen('lsof -i:%s' % port).readlines()
    regex = re.compile('\s+')
    process_id_list = []
    if len(process_detail_list) > 1:
        for process_detail in process_detail_list:
            process = regex.split(process_detail)
            process_id = process[1]
            if process_id.isdigit():
                process_id_list.append(process_id)

    for pid in set(process_id_list):
        try:
            print pid
            os.system('kill -9 %s' % pid)
        except Exception as e:
            print e


if __name__ == '__main__':
    params = sys.argv
    if len(params) == 2 and params[1].isdigit():
        kill_process(params[1])
    else:
        print '请输入端口号'
