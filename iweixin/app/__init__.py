# coding:utf-8
from tornado import web


class BaseHandler(web.RequestHandler):
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)
