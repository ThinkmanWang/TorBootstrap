# -*- coding: UTF-8 -*-

import sys
import os

from pythinkutils.aio.auth.tornado.handler.BaseSimpleAuthHandler import *

class TestHandler(BaseSimpleAuthHandler):

    @page_login_required()
    async def get(self):
        self.render("bussiness_all_data_collect.html", info="Hello World", title_insert = "FXXK", username_insert="FXXK1")
        # self.write("HOMEPAGE To be continued...")