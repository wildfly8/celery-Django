from celery import shared_task
from time import sleep

@shared_task
def hello():
    sleep(5)
    return "Hello Celery!"
