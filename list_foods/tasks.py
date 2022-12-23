from time import sleep
from celery import shared_task

@shared_task
def my_task():
    sleep(5)
    return {'name':'gustav'}

