from django.shortcuts import render
from alunos.models import Aluno

def index(request):

    todos_alunos = Aluno.objects.all()

    context = {
        "nome_pagina": "Início",
        "todos_alunos": todos_alunos,
    }
    return render(request, "index.html", context)
