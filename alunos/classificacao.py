"""###ETAPA_6: Salvar modelo treinado """

from django.shortcuts import render, redirect
from alunos.forms import AlunoForm
import os
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler


def classificacao(request):
    form = AlunoForm()

    if request.method == "POST":
        form = AlunoForm(request.POST)

        if form.is_valid():
            # aluno = form.save(commit=False)
            # aluno.registrado_por = request.user.docente
            # aluno.save()
            # return redirect("index")
            # importar modelo
            rede_neural = pickle.load(open('../static/rna/!rede_neural_finalizado.sav', 'rb'))

            # novo_registro = previsores[38]
            novo_registro = form
            novo_registro = novo_registro.reshape(1, -1)
            print(novo_registro)
            print(novo_registro.shape)

            # 1 = evasão
            # resposta = rede_neural.predict(novo_registro)
            #
            # if resposta[0] == 0:
            #     print('Não evasão')
            # else:
            #     print('Evasão')
            #
            # probabilidade_resposta = rede_neural.predict_proba(novo_registro)
            # print(probabilidade_resposta)
            #
            # confianca = probabilidade_resposta.max()
            # print(confianca)

            # base_4.columns

    context = {
        "nome_pagina": "clasfificacao",
        "form": form
    }

    return render(request, "resultado.html", context)
