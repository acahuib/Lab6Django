from django.contrib import admin
from .models import Alumno, Curso, NotasAlumnosPorCurso

admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(NotasAlumnosPorCurso)

