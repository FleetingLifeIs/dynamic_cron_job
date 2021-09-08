from __future__ import absolute_import, unicode_literals
import os

from celery import Celery, platforms
from django.utils.datetime_safe import datetime

# 获取当前文件夹名，即为该 Django 的项目名
project_name = os.path.split(os.path.abspath('.'))[-1]
project_settings = '%s.settings' % project_name
print(project_settings)

# 设置默认celery命令行的环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_celery.settings')

# 实例化 Celery,项目名称
app = Celery('Django_celery')

# 解决时区问题
app.now = datetime.now

# 使用 django 的 settings 文件配置 celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# 从所有应用中加载任务模块tasks.py
app.autodiscover_tasks()

# 解决celery不能root用户启动的问题
platforms.C_FORCE_ROOT = True
