from django.urls import path

from api.views import add_view, subtract_view, multiply_view, divide_view

app_name = 'api'

urlpatterns = [
    path('add/', add_view, name='add'),
    path('subtract/', subtract_view, name='sub'),
    path('multiply/', multiply_view, name='mul'),
    path('divide/', divide_view, name='div'),
]