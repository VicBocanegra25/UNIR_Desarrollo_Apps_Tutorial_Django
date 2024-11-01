from django.urls import path

from .views import pagina_web_inicial

urlpatterns = [
    path("", pagina_web_inicial),
]
