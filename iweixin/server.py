# coding:utf-8
from tornado import web, ioloop, httpserver
from tornado.options import options, define
from urls import urlpatterns
import os

define("port", default=8888, type=int, help='run server on this port')


class Application(web.Application):
    def __int__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)


if __name__ == '__main__':
    app = Application(
        urlpatterns,
        static_path=os.path.join(os.path.dirname(__file__), "statics"),
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        cookie_secret="WEIXIN_COOKIE_SECRET_TEST",
        debug=True,
    )
    http_server = httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print 'http://127.0.0.1:%s' % options.port
    ioloop.IOLoop.current().start()
