import json

from django.http import HttpResponseNotAllowed, HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


def add_view(request, *args, **kwargs):
    ans = None
    if request.body:
        data = json.loads(request.body)
        ans = data['A'] + data['B']
    answer = {
        'content': ans
    }
    return JsonResponse(answer)


def subtract_view(request, *args, **kwargs):
    ans = None
    if request.body:
        data = json.loads(request.body)
        ans = data['A'] - data['B']
    answer = {
        'content': ans
    }
    return JsonResponse(answer)


def multiply_view(request, *args, **kwargs):
    ans = None
    if request.body:
        data = json.loads(request.body)
        ans = data['A'] * data['B']
    answer = {
        'content': ans
    }
    return JsonResponse(answer)


def divide_view(request, *args, **kwargs):
    ans = None
    if request.body:
        data = json.loads(request.body)
        ans = data['A'] / data['B']
    answer = {
        'content': ans
    }
    return JsonResponse(answer)