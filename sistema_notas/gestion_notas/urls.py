from django.urls import path
from . import views

urlpatterns = [
    path('alumnos/', views.listar_alumnos, name='listar_alumnos'),
    path('alumnos/nuevo/', views.nuevo_alumno, name='nuevo_alumno'),
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('cursos/nuevo/', views.nuevo_curso, name='nuevo_curso'),
    path('notas/', views.listar_notas, name='listar_notas'),
    path('notas/nueva/', views.nueva_nota, name='nueva_nota'),
]

