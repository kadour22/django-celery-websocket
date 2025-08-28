from django.http import HttpResponse
from .tasks import say_hello_task
def index(request) :
    task = say_hello_task.delay()
    return HttpResponse(task)