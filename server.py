# _*_coding=UTF-8_*_
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os, sys
from core import app

from config.logConfig import logConfigInit

from tornado.options import define, options
from server.websocket.chat import ChatConnection
from server.websocket.message import MessageConnection
import sockjs

define("port", default=9004, help="run on the given port", type=int)



application = app.Application()
application.autoLoadModule(os.path.join(sys.path[0], "server"))

# 添加sockjs
ChatRouter = sockjs.tornado.SockJSRouter(ChatConnection, '/chat')
application.add_handlers(".*$",ChatRouter.urls)

MessageRouter = sockjs.tornado.SockJSRouter(MessageConnection, '/message')
application.add_handlers(".*$",MessageRouter.urls)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    logConfigInit()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

define("logging", default="debug",metavar="debug|info|warning|error|none")
