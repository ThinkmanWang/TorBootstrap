# -*- coding: UTF-8 -*-

import sys
import os

from pythinkutils.aio.auth.tornado.handler.BaseSimpleAuthHandler import *
from pythinkutils.common.object2json import *

class MainHandler(BaseSimpleAuthHandler):

    @classmethod
    def func_test(cls):
        return "TEEEEEEEST FXXXXXXXXXXXXXXXK"

    @page_login_required()
    async def get(self):
        self.render("index.html", info="Hello World", title_insert = "FXXK", username_insert="FXXK1")
        # self.write("HOMEPAGE To be continued...")

        self.request.full_url()

def hello():
    return "Hello World"