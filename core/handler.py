# -*- coding:utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement

import functools
import time, json
import weakref

import tornado.web
from tornado import escape,gen
from core.client import AsyncClient


class BaseHandler(tornado.web.RequestHandler):
    url_pattern = None

    def __init__(self, application, request, **kwargs):
        self.client = AsyncClient()  # AsyncClient
        super(BaseHandler, self).__init__(application, request, **kwargs)

    def get_current_user(self):
        return self.get_cookie("userId")

    def prepare(self):
        allowURL = ["Login","login"]
        a = self.request
        for url in allowURL:
            if url in self.request.path:
                return
        #if not self.current_user:  # all api require login
        #    self.redirect("/login")
        #else:
        #    return
        return

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Allow-Headers', '*')
        #self.set_header('Content-type', 'application/json') #此行导致中文乱码

    # below is self use methods
    def getParmas(self):
        return json.loads(self.request.body)