# -*- coding: UTF-8 -*-

import sys
import os

from pythinkutils.aio.auth.tornado.handler.BaseSimpleAuthHandler import *

class LogoutHandler(BaseSimpleAuthHandler):
    async def post(self):
        await self.logout()
        self.redirect("/login")

    async def get(self):
        await self.post()