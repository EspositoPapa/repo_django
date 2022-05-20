from django.urls import path,include
from.import views

urlpatterns = [
    path("cursos", views.cursos),
    path("alta_curso/<nombre>",views.alta_curso)
]
