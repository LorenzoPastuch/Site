from .views import Homepage, Minhahistoria, Meusdados, Meuportifolio
from django.urls import path

app_name = 'lorenzo'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('minhahistoria/<int:pk>', Minhahistoria.as_view(), name='minhahistoria'),
    path('meusdados/<int:pk>', Meusdados.as_view(), name='meusdados'),
    path('meuportifolio/', Meuportifolio.as_view(), name='meuportifolio')
]