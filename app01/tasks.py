from __future__ import absolute_import, unicode_literals
from Django_celery.celeryconfig import app


@app.task
def plan_task_1():
    print("任务_1已运行！")
    return {"任务_1:success"}


@app.task
def plan_task_2():
    print("任务_2已运行！")
    return {"任务_2:success"}
