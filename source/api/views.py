import json

from django.http import JsonResponse


def add_view(request, *args, **kwargs):
    if request.body:
        data = json.loads(request.body)
        try:
            answer = float(data['A']) + float(data['B'])
        except Exception as e:
            return JsonResponse({'error': str(e)})
        return JsonResponse({'result': str(answer)})


def subtract_view(request, *args, **kwargs):
    if request.body:
        data = json.loads(request.body)
        try:
            answer = float(data['A']) - float(data['B'])
        except Exception as e:
            return JsonResponse({'error': str(e)})
        return JsonResponse({'result': str(answer)})


def multiply_view(request, *args, **kwargs):
    if request.body:
        data = json.loads(request.body)
        try:
            answer = float(data['A']) * float(data['B'])
        except Exception as e:
            return JsonResponse({'error': str(e)})
        return JsonResponse({'result': str(answer)})


def divide_view(request, *args, **kwargs):
    if request.body:
        data = json.loads(request.body)
        try:
            answer = float(data['A']) / float(data['B'])
        except Exception as e:
            return JsonResponse({'error': str(e)})
        return JsonResponse({'result': str(answer)})