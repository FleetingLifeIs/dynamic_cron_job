# dynamic_cron_job
**基于django celery admin 的动态定时任务系统**

python 3.6.8 

windows 10

Django 2.2

celery 4.4.7

```python
# 安装相关package
pip install -r requirements.txt

# 配置数据库
settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # 根据自己的数据库进行配置
        'NAME': 'your database',
        'HOST': 'your HOST',
        'POST': 'your PORT',
        'USER': 'your user',
        'PASSWORD': 'your password',
    }
}

# 在项目根目录下执行数据库迁移指令
python manager.py makemigrations
python manager.py migrate

# 创建admin 超级管理员
python manager.py createsuperuser

# 启动celery worker 和 beat
celery -A dynamic_cron_job beat -l info
celery worker -A dynamic_cron_job -l info -P eventlet

# 启动项目
python manager.py runserver

# 访问
http://127.0.0.1:8000/admin
```






