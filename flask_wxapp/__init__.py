# -*- coding: utf-8 -*-
import base64
import json
import requests
from Crypto.Cipher import AES


class WXApp(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.appid = app.config['WX_APPID']
        self.secret = app.config['WX_SECRET']

    def jscode2session(self, js_code):
        url = ('https://api.weixin.qq.com/sns/jscode2session?'
               'appid={}&secret={}&js_code={}&grant_type=authorization_code'
               ).format(self.appid, self.secret, js_code)
        r = requests.get(url)
        return r.json()

    def decrypt(self, session_key, encrypted_data, iv):
        # base64 decode
        session_key = base64.b64decode(session_key)
        encrypted_data = base64.b64decode(encrypted_data)
        iv = base64.b64decode(iv)

        cipher = AES.new(session_key, AES.MODE_CBC, iv)

        decrypt_data = self._unpad(cipher.decrypt(encrypted_data))
        decrypted = json.loads(decrypt_data.decode())

        if decrypted['watermark']['appid'] != self.appid:
            raise Exception('Invalid Buffer')

        return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]
