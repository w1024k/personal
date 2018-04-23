# coding: utf-8

import requests, sys
from lxml import etree
from sina_nba import settings
import time


class Score(object):
    def __init__(self, url=None, rate=0):
        self.url = url or settings.SCORE_URL
        self.rate = rate

    # rate = raw_input("刷新频率(秒):")
    # try:
    #     rate = int(rate)
    # except:
    #     rate = 0
    def get_score(self):
        params = {
            "vt": 4,
            "livetype": "nba",
        }
        index_text = requests.get(url=self.url, params=params, headers=settings.HEADERS).text
        selector = etree.HTML(index_text)
        detail = selector.xpath("//h2[@class='live_h2']/a/text()")
        sys.stdout.write(' '.join(detail).encode('utf-8') + "\r")
        sys.stdout.flush()

    def run(self):
        if self.rate == 0:
            self.get_score()
        else:
            while True:
                self.get_score()
                time.sleep(self.rate)
