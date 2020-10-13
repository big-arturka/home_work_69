from django.urls import path

from api.views import get_token_view, add_view, subtract_view, multiply_view, divide_view

app_name = 'api'

urlpatterns = [
    path('get_token/', get_token_view),
    path('add/', add_view),
    path('subtract/', subtract_view),
    path('multiply/', multiply_view),
    path('divide/', divide_view),
]