import codecs

from django.shortcuts import render, redirect
from alunos.forms import AlunoForm

"""###ETAPA_6: Salvar modelo treinado """
import os
import pickle
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

def registrar_aluno(request):

    form = AlunoForm()

    if request.method == "POST":
        form = AlunoForm(request.POST)

        if form.is_valid():
            aluno = form.save(commit=False)

            aluno.registrado_por = request.user.docente

            # aluno.save()

            return redirect("index")

    context = {
        "nome_pagina": "Registrar aluno",
        "form": form
    }

    return render(request, "registrar_aluno.html", context)


def classificacao(request):
    form = AlunoForm()
    classificado = ''
    confianca = ''

    if request.method == "POST":
        form = AlunoForm(request.POST)

        if form.is_valid():
            # aluno = form.save(commit=False)
            # aluno.registrado_por = request.user.docente
            # aluno.save()
            # return redirect("index")
            # importar modelo
            print(form.cleaned_data)
            print(form.clean())
            print(form.changed_data)
            novo_registro = pd.DataFrame.from_dict(form.clean(), orient='index')

            novo_registro = novo_registro.T

            print("****** novo registro")
            print(novo_registro)

            previsores = pd.read_csv(r"static/rna/escala-min-max/!base-modelo-django.csv", encoding="utf-8-sig")

            print("****** base modelo")
            print(previsores)

            novo_registro.columns = previsores.columns
            previsores = pd.concat([previsores, novo_registro], axis=0, ignore_index=True)

            previsores = previsores.iloc[:, 0:15].values
            print("****** base modelo com novo registro")
            print(previsores)

            # Transformação de atributos categóricos em numéricos
            labelencoder_previsores = pickle.load(open(r"static/rna/escala-min-max/!labelencoder-previsores-min-max", "rb"))

            previsores[:, 2] = labelencoder_previsores.fit_transform(previsores[:, 2])
            previsores[:, 4] = labelencoder_previsores.fit_transform(previsores[:, 4])
            previsores[:, 6] = labelencoder_previsores.fit_transform(previsores[:, 6])
            previsores[:, 9] = labelencoder_previsores.fit_transform(previsores[:, 9])
            previsores[:, 13] = labelencoder_previsores.fit_transform(previsores[:, 13])
            previsores[:, 14] = labelencoder_previsores.fit_transform(previsores[:, 14])

            print("****** label encoder")
            print(previsores)
            print(previsores.shape)

            # Dummy codificação de valores, onde cada variável se torna uma coluna
            onehotencoder_previsores = pickle.load(open(r"static/rna/escala-min-max/!onehotencoder-previsores-min-max", "rb"))
            previsores = onehotencoder_previsores.fit_transform(previsores)

            print("****** onehot encoder")
            print(previsores)
            print(previsores.shape)

            # Escalonamento dos dados, para dispo-los em mesma base, evitando viés
            min_max_scaler = MinMaxScaler()
            previsores = min_max_scaler.fit_transform(previsores)

            print("****** scaler min max previsores")
            print(previsores)
            print(previsores.shape)

            rede_neural = pickle.load(open(r"static/rna/escala-min-max/!rede_neural_finalizado-min-max.sav", "rb"))

            novo_registro = previsores[14]
            novo_registro = novo_registro.reshape(1, -1)
            print(novo_registro)
            print(novo_registro.shape)

            # 1 = evasão
            resposta = rede_neural.predict(novo_registro)
            #
            if resposta[0] == 0:
                classificado = 'Não evasão'
                print('Não evasão')
            else:
                classificado = 'Evasão'
                print('Evasão')

            probabilidade_resposta = rede_neural.predict_proba(novo_registro)
            print("****** probabilidade")
            print(probabilidade_resposta)

            confianca = probabilidade_resposta.max()
            print("****** confiança")
            print(confianca)
            confianca = confianca*100
            confianca = int(confianca)
            # base_4.columns

            # return redirect("classificacao")

    context = {
        "nome_pagina": "Previsão da situação do estudante",
        "form": form,
        "resposta": classificado,
        "confianca": confianca

    }

    return render(request, "classificacao.html", context)