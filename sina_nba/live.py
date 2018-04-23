import websocket
import requests, time, json
from sina_nba import settings


class Live(object):
    def __init__(self, roomnum):
        self.roomnum = roomnum

    def on_message(self, ws, message):
        rsp = json.loads(message)
        detail = rsp.get("c") or rsp.get("b")
        match = detail.get("match")
        if match:
            print "%s [%s : %s]" % (match["phase"], match["score1"], match["score2"])

        print "%s: %s" % (detail["liver"]["nickname"], detail.get("text"))

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")

    def get_verify(self):
        params = {
            "roomnum": "sports:%s" % self.roomnum,
            "_": str(int(time.time() * 1000))
        }
        verify = requests.get(url=settings.VERIFY_URL, params=params).json()['result']['data']
        return verify

    def run(self):
        websocket.WebSocket()
        websocket.enableTrace(True)

        ws = websocket.WebSocketApp(
            settings.LIVE_WS + self.get_verify(),
            header=settings.WS_HEADERS,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        ws.run_forever()

