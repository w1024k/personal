# coding: utf-8

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}

WS_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Origin": 'http://sports.sina.cn',
    'Sec-WebSocket-Protocol': 'null',
}

# 比分
SCORE_URL = "http://lives.sina.cn/"

# 直播签名
VERIFY_URL = "http://rapid.sports.sina.com.cn/home/api/room/socketverify"

# 直播
LIVE_WS = "ws://ably.sports.sina.com.cn/"
