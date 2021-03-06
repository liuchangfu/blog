from django.apps import AppConfig
import os

default_app_config = 'account.PrimaryAccountConfig'

VERBOSE_APP_NAME = "帐户管理"


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class PrimaryAccountConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME
