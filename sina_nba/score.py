# coding: utf-8

import requests, sys
from lxml import etree
import settings
import time


class Score(object):
    def __init__(self, url=None):
        self.url = url or settings.SCORE_URL

    def get_node(self):
        params = {
            "vt": 4,
            "livetype": "nba",
        }
        index_text = requests.get(url=self.url, params=params, headers=settings.HEADERS).text
        selector = etree.HTML(index_text)
        node = selector.xpath('//h2[@class ="live_h2"]/a')
        return node

    def get_score(self):

        node = self.get_node()
        score_list = list()

        for node1 in node:
            score = node1.xpath(".//text()")[0]
            score_list.append(score)

            # sys.stdout.write(' '.join(score_list).encode('utf-8') + "\r")
            # sys.stdout.flush()

    def get_rooms(self):
        node = self.get_node()
        room_id_list = []
        for index, node1 in enumerate(node):
            score = node1.xpath(".//text()")[0]
            links = node1.xpath(".//@href")[0]
            print index, score

            room_id = links.split("=")[-1]
            room_id_list.append(room_id)
        num = raw_input('please choose live')
        return num

    def run(self, rate='start'):
        if rate == 'start':
            rate = 0
        else:
            rate = raw_input("刷新频率(秒):")
            try:
                rate = int(rate)
            except:
                rate = 0

        if rate == 0:
            self.get_score()
        else:
            while True:
                self.get_score()
                time.sleep(rate)
