# -*- coding: utf-8 -*-
"""
    flaskext.methodhack
    ~~~~~~~~~~~~~~~~~~~

    A extension to Flask for `PUT` and `DELETE` method hack.

    :copyright: (c) 2010 by Kijun Seo <kijun@lunant.net>.
    :license: BSD, see LICENSE for more details.
"""

class MethodHack(object):
    """

    Example::

        from flaskext.methodhack import MethodHack
        app = Flask(__name__)
        app.wsgi_app = MethodHack(app.wsgi_app)

    :param override_param: Parameter name used to override default method.
                           Initialized to `__method__`
    :param override_get: Used for sites like Facebook which makes a GET request
                         on a provided address when the user deletes an app.
                         Initialized to :class:`False`.

    """

    def __init__(self, wsgi_app, override_param="__method__",
                 override_get=False):
        self.wsgi_app = wsgi_app
        self.override_param = override_param
        self.override_get = override_get


    def __call__(self, environ, start_response):
        method = environ.method.upper()
        if method == "POST":
            if self.override_param in environ.form:
                environ.method = environ.form[self.override_param].upper()
        elif override_get and method == "GET":
            if self.override_param in self.environ.args:
                environ.method = environ.args[self.override_param].upper()
        return self.wsgi_app(self, environ, start_response)
