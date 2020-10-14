import json

from django.http import JsonResponse


def add_view(request, *args, **kwargs):
    ans = None
    if request.body:
        data = json.loads(request.body)
        ans = int(data['A']) + int(data['B'])
    answer = {
        'result': str(ans)
    }
    return JsonResponse(answer)


def subtract_view(request, *args, **kwargs):
    ans = None
    if request.body:
        data = json.loads(request.body)
        ans = int(data['A']) - int(data['B'])
    answer = {
        'result': str(ans)
    }
    return JsonResponse(answer)


def multiply_view(request, *args, **kwargs):
    ans = None
    if request.body:
        data = json.loads(request.body)
        ans = int(data['A']) * int(data['B'])
    answer = {
        'result': str(ans)
    }
    return JsonResponse(answer)


def divide_view(request, *args, **kwargs):
    ans = None
    if request.body:
        data = json.loads(request.body)
        ans = int(data['A']) / int(data['B'])
    answer = {
        'result': str(ans)
    }
    return JsonResponse(answer)

