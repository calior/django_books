# -*-coding:utf-8-*-
from django.apps import AppConfig
from os import path

VERBOSE_APP_NAME = u"书籍管理"


def get_current_app_name(_file):
    return path.split(path.dirname(_file))[-1]
    #return path.dirname(_file).replace('\\', '/').split('/')[-1]


class BooksConfig(AppConfig):

    name = get_current_app_name(__file__)
    verbose_app_name = VERBOSE_APP_NAME

# default_app_config = get_current_app_name(__file__) + '.__init__.BooksConfig'
