from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, NotasAlumnosPorCursoForm
from .models import Alumno, Curso, NotasAlumnosPorCurso

def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'gestion_notas/listar_alumnos.html', {'alumnos': alumnos})

def nuevo_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos')  # Corregir la redirección
    else:
        form = AlumnoForm()
    return render(request, 'gestion_notas/nuevo_alumno.html', {'form': form})

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'gestion_notas/listar_cursos.html', {'cursos': cursos})

def nuevo_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'gestion_notas/nuevo_curso.html', {'form': form})

def listar_notas(request):
    notas = NotasAlumnosPorCurso.objects.all()
    return render(request, 'gestion_notas/listar_notas.html', {'notas': notas})

def nueva_nota(request):
    if request.method == "POST":
        form = NotasAlumnosPorCursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_notas')
    else:
        form = NotasAlumnosPorCursoForm()
    return render(request, 'gestion_notas/nueva_nota.html', {'form': form})

