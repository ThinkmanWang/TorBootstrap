# -*- coding: UTF-8 -*-

import sys
import os

from pythinkutils.aio.auth.tornado.handler.BaseSimpleAuthHandler import *

class LoginHandler(BaseSimpleAuthHandler):

    async def post(self):
        szUsername = self.get_argument("username", "")
        szPwd = self.get_argument("password", "")
        szRedirectUrl = self.get_argument("redirect_url", "")

        if is_empty_string(szUsername) or is_empty_string(szPwd):
            self.write('''
                    <form action="/login" method="POST">
                        <p>Username: <input type="text" name="username" /></p>
                        <p>Password: <input type="text" name="password" /></p>
                        <p><input type="hidden" name="redirect_url" value="{}" /></p>
                        <input type="submit" value="Submit" />
                    </form>
                    '''.format(szRedirectUrl))
        else:
            nUID, _szUsername, szToken = await self.login(szUsername, szPwd)
            if False == is_empty_string(szToken):
                if is_empty_string(szRedirectUrl):
                    self.redirect("/")
                else:
                    self.redirect(szRedirectUrl)
            else:
                self.redirect("/login")

    async def get(self):
        await self.post()