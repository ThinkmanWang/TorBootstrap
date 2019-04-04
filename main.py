# -*- coding: UTF-8 -*-

import sys
import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado import gen
import aiomysql

from tornado.httpserver import HTTPServer
from tornado.platform.asyncio import AsyncIOMainLoop
import asyncio

from pythinkutils.common.log import g_logger
from pythinkutils.aio.auth.tornado.handler.BaseSimpleAuthHandler import *
from pythinkutils.common.StringUtils import *

from handler.MainHandler import MainHandler
from handler.LoginHandler import LoginHandler
from handler.LogoutHandler import LogoutHandler

application = tornado.web.Application(handlers = [
    (r"/login", LoginHandler)
    , (r'/', MainHandler)
    , (r"/logout", LogoutHandler)
], autoreload=False)

async def on_server_started():
    g_logger.info("Server Started!")

if __name__ == '__main__':

    http_server = HTTPServer(application)
    http_server.bind(8590)
    http_server.start(0)

    # ipDB = IPLocation.instance()
    g_logger.info('HTTP Server started... %d' % (os.getpid(),))
    asyncio.gather(on_server_started())

    tornado.ioloop.IOLoop.current().start()