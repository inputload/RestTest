from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view()),  # Путь который отобразит MainView
    path('sum/', SumView.as_view()),  # +
    path('cur/', BankView.as_view()),  # +
]
