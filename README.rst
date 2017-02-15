微信小程序Flask扩展
===================

- `微信文档 <https://mp.weixin.qq.com/debug/wxadoc/dev/api/api-login.html>`_

Configuration
-------------

Your configuration should be declared within your Flask config. 

.. code:: python

    WX_APPID = 'your appid'
    WX_SECRET = 'your app secret'

Create instance within your application

.. code:: python

    from flask import Flask
    from flask_wxapp import WXApp

    wxapp = WXApp()

    def create_app():
        app = Flask(__name__)
        wxapp.init_app(app)
        return app

Usage
-----

- 通过code换取openid和session_key

接口::

  wxapp.jscode2session(js_code)

返回json(dict):

============    =============
参数            说明
============    =============
openid          用户唯一标识
session_key     会话密钥
============    =============


- 加密数据解密

接口::

    wxapp.decrypt(session_key, encrypted_data, iv)

返回数据如下::

    {
	'avatarUrl': 'http://wx.qlogo.cn/mmopen/vi_32/aSKcBBPpibyKNicHNTMM0qJVh8Kjgiak2AHWr8MHM4WgMEm7GFhsf8OYrySdbvAMvTsw3mo8ibKicsnfN5pRjl1p8HQ/0',
	'city': 'Guangzhou',
	'country': 'CN',
	'gender': 1,
	'language': 'zh_CN',
	'nickName': 'Band',
	'openId': 'oGZUI0egBJY1zhBYw2KhdUfwVJJE',
	'province': 'Guangdong',
	'unionId': 'ocMvos6NjeKLIBqg5Mr9QjxrP1FA',
	'watermark': {'appid': 'wx4f4bc4dec97d474b', 'timestamp': 1477314187}
    }


