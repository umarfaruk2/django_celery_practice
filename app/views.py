from django.shortcuts import render
from django_celery.celery import add
from .tasks import sub, multi
from celery.result import AsyncResult

"""
    for start celery worker apply bellow command

    celery -A project_name worker -l info
"""

# Enqueue Task using delay()
# def index(request):
#     print('Result: ')
#     result_1 = add.delay(10, 20)
#     result_2 = sub.delay(10, 20)
#     print("result: ", result_2)
#     return render(request, 'app/home.html')

# Enqueue Task using apply_async()
# def index(request):
#     print('Result: ')
#     result_2 = sub.apply_async(args=[10, 30])
#     print("result: ", result_2)
#     return render(request, 'app/home.html')

# Display addition value after task execution
def index(request):
    result = multi.delay(10, 20) 
    return render(request, 'app/home.html', {'result': result})

def check_result(request, task_id):
    # retrieve the task result using the task_id
    result = AsyncResult(task_id)

    return render(request, 'app/result.html', {'result': result})
    
def about(request):
    print('Result: ')
    return render(request, 'app/about.html')

def contact(request):
    print('Result: ')
    return render(request, 'app/contact.html')