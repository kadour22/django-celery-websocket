from celery import shared_task

@shared_task
def say_hello_task() :
    return "Hello from celery"