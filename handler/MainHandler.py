# -*- coding: UTF-8 -*-

import sys
import os

from pythinkutils.aio.auth.tornado.handler.BaseSimpleAuthHandler import *

class MainHandler(BaseSimpleAuthHandler):

    @page_login_required()
    async def get(self):
        self.write("HOMEPAGE To be continued...")