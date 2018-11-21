#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Display document description information
编译环境: Python


"""
__author__ = 'LoveLinXue.com'

import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')


# 生产环境配置

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
    DEBUG = False


# 开发环境配置

class DevelopmentConfig(Config):
    DEBUG = True


# 测试环境配置

class TestingConfig(Config):
    TESTING = True

# CSRF_ENABLED = True
# SECRET_KEY = 'you-will-never-guess'



#默认配置参数

# {
#     'DEBUG':                                get_debug_flag(default=False),  是否开启Debug模式
#     'TESTING':                              False,                          是否开启测试模式
#     'PROPAGATE_EXCEPTIONS':                 None,
#     'PRESERVE_CONTEXT_ON_EXCEPTION':        None,
#     'SECRET_KEY':                           None,
#     'PERMANENT_SESSION_LIFETIME':           timedelta(days=31),
#     'USE_X_SENDFILE':                       False,
#     'LOGGER_NAME':                          None,
#     'LOGGER_HANDLER_POLICY':               'always',
#     'SERVER_NAME':                          None,
#     'APPLICATION_ROOT':                     None,
#     'SESSION_COOKIE_NAME':                  'session',
#     'SESSION_COOKIE_DOMAIN':                None,
#     'SESSION_COOKIE_PATH':                  None,
#     'SESSION_COOKIE_HTTPONLY':              True,
#     'SESSION_COOKIE_SECURE':                False,
#     'SESSION_REFRESH_EACH_REQUEST':         True,
#     'MAX_CONTENT_LENGTH':                   None,
#     'SEND_FILE_MAX_AGE_DEFAULT':            timedelta(hours=12),
#     'TRAP_BAD_REQUEST_ERRORS':              False,
#     'TRAP_HTTP_EXCEPTIONS':                 False,
#     'EXPLAIN_TEMPLATE_LOADING':             False,
#     'PREFERRED_URL_SCHEME':                 'http',
#     'JSON_AS_ASCII':                        True,
#     'JSON_SORT_KEYS':                       True,
#     'JSONIFY_PRETTYPRINT_REGULAR':          True,
#     'JSONIFY_MIMETYPE':                     'application/json',
#     'TEMPLATES_AUTO_RELOAD':                None,
# }
