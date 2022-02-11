from django.contrib import admin
from django.urls import path

from usuarios.views import index
from alunos.views import registrar_aluno
from alunos.views import classificacao

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "",
        index,
        name = "index",
    ),

    path(
        "registrar-aluno/",
        registrar_aluno,
        name = "registrar_aluno",
    ),
    path(
        "classificacao/",
        classificacao,
        name = "classificacao",
    ),
]
