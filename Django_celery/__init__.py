# 引入celery实例对象
from __future__ import absolute_import, unicode_literals
from Django_celery.celeryconfig import app as celery_app

__all__ = ('celery_app',)
