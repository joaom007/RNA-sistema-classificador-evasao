from django.db import models


class Aluno(models.Model):

    ano_conclusao_anterior = models.PositiveSmallIntegerField(
        verbose_name="Ano de Conclusão do Ensino Anterior"
    )
    distancia_campus = models.FloatField(
        verbose_name="Distância do Câmpus (km)",
        max_length=7
    )
    NIVEL_ENSINO_CHOICES = (
        ('Graduação', 'Graduação'), ('Médio', 'Médio'), ('Pós-graduação', 'Pós-graduação'))

    nivel_ensino = models.CharField(
        verbose_name="Nível de Ensino",
        max_length=20,
        choices=NIVEL_ENSINO_CHOICES,
        blank=False,
        null=False
    )
    PERIODO_CHOICES = (
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
        ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'))
    periodo_atual = models.CharField(
        verbose_name="Período Atual",
        max_length=1,
        choices=PERIODO_CHOICES,
        blank=False,
        null=False

    )
    TURNO_CHOICES = (
        ('Integral', 'Integral'), ('Matutino', 'Matutino'), ('Noturno', 'Noturno'), ('Vespertino', 'Vespertino'))
    turno = models.CharField(
        verbose_name="Turno",
        max_length=15,
        choices=TURNO_CHOICES,
        blank=False,
        null=False
    )
    ANO_CHOICES = (
    ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'),
    ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'),
    ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'))

    ano_previsao_conclusao = models.CharField(
        verbose_name="Ano Letivo de Previsão de Conclusão",
        max_length=4,
        choices = ANO_CHOICES,
        blank=False,
        null=False
    )
    CURSO_CHOICES = (('ITP.BAC.MEC.2016','BACHARELADO EM ENGENHARIA MECÂNICA'), ('ITP.INT.ELM.2016','TÉCNICO EM ELETROMECÂNICA'),
                     ('ITP.INT.INF.2016','TÉCNICO EM INFORMÁTICA INTEGRADO AO ENSINO MÉDIO'), ('ITP.INT.SEE.INF.2013','TÉCNICO EM ELETROMECÂNICA INTEGRADO AO ENSINO MÉDIO'),
                     ('ITP.LAT.IAE.2016','PÓS GRADUAÇÃO LATO SENSU EM INFORMÁTICA APLICADA À EDUCAÇÃO'), ('ITP.LIC.FDB.2011','PROGRAMA ESPECIAL DE FORMAÇÃO DE DOCENTES PARA A EDUCAÇÃO BÁSICA'),
                     ('ITP.LIC.FIS.2010','LICENCIATURA EM FÍSICA'), ('ITP.LIC.MAT.2016','LICENCIATURA EM MATEMÁTICA'),
                     ('ITP.TEC.EDF.2011','TÉCNICO EM EDIFICAÇÕES'), ('ITP.TEC.INF.2019','TÉCNICO EM INFORMÁTICA'),
                     ('ITP.TEC.MEC.2010','TÉCNICO EM MECÂNICA'), ('ITP.TEC.MSI.2010','TÉCNICO EM MANUTENÇÃO E SUPORTE EM INFORMÁTICA'))

    codigo_curso = models.CharField(
        verbose_name="Código Curso",
        max_length=100,
        choices=CURSO_CHOICES,
        blank=False,
        null=False
    )


    ano_matricula = models.CharField(
        verbose_name="Ano de Matrícula",
        max_length=4,
        choices = ANO_CHOICES,
        blank=False,
        null=False
    )
    idade = models.PositiveSmallIntegerField(
        verbose_name="Idade"
    )
    ETNIA_CHOICES = (('Não declarado', 'Não declarado'), ('Amarela', 'Amarela'),
                     ('Branca', 'Branca'), ('Indígena', 'Indígena'), ('Parda', 'Parda'), ('Preta', 'Preta'))

    etnia = models.CharField(
        verbose_name="Etnia/Raça",
        max_length=20,
        choices=ETNIA_CHOICES,
        blank=False,
        null=False
    )
    frequencia = models.FloatField(
        verbose_name="Frequência no Período",
        max_length=5
    )
    ira = models.FloatField(
        verbose_name="I.R.A.",
        max_length=4
    )
    progresso = models.FloatField(
        verbose_name="Percentual de Progresso",
        max_length=5
    )
    SEXO_CHOICES = (("F", "Feminino"), ("M", "Masculino"))

    sexo = models.CharField(
        verbose_name="Sexo",
        max_length=1,
        choices = SEXO_CHOICES,
        blank=False,
        null=False
    )

    ESCOLA_CHOICES = (('Pública', 'Pública'), ('Privada', 'Privada'))

    tipo_escola_origem = models.CharField(
        verbose_name="Tipo de Escola de Origem",
        max_length = 15,
        choices = ESCOLA_CHOICES,
        blank=False,
        null=False
    )

    # horario_registro = models.DateTimeField(
    #     verbose_name="Horário de registro",
    #     auto_now_add=True
    # )
    #
    # registrado_por = models.ForeignKey(
    #     "docentes.Docente",
    #     verbose_name="Docente responsável pelo registro",
    #     on_delete=models.PROTECT
    # )

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        db_table = "aluno"

    def __str__(self):
        return self.codigo_curso
# from django.db import models
#
#
# class Aluno(models.Model):
#     school = models.CharField(
#         verbose_name="Escola",
#         max_length=10
#     )
#
#     sex = models.CharField(
#         verbose_name="Sexo",
#         max_length=10
#     )
#
#     age = models.PositiveSmallIntegerField(
#         verbose_name="Idade",
#     )
#
#     address = models.CharField(
#         verbose_name="Endereço",
#         max_length=10
#     )
#
#     famsize = models.CharField(
#         verbose_name="Tamanho da família",
#         max_length=3,
#     )
#
#     pstatus = models.CharField(
#         verbose_name="Coabitação",
#         max_length=10
#     )
#
#     medu = models.PositiveSmallIntegerField(
#         verbose_name="Educação da mãe",
#     )
#
#     fedu = models.PositiveSmallIntegerField(
#         verbose_name="Educação do pai",
#     )
#
#     mjob = models.CharField(
#         verbose_name="Trabalho da mãe",
#         max_length=50
#     )
#
#     fjob = models.CharField(
#         verbose_name="Trabalho do pai",
#         max_length=50
#     )
#
#     reason = models.CharField(
#         verbose_name="Razão de escolha da escola",
#         max_length=50
#     )
#
#     guardian = models.CharField(
#         verbose_name="Guardião",
#         max_length=50
#     )
#
#     traveltime = models.PositiveSmallIntegerField(
#         verbose_name="Tempo de viagem, casa escola",
#     )
#
#     studytime = models.PositiveSmallIntegerField(
#         verbose_name="Horas de estudo, semanal",
#     )
#
#     failures = models.PositiveSmallIntegerField(
#         verbose_name="Reprovações",
#     )
#
#     schoolup = models.CharField(
#         verbose_name="Suporte educacional extra",
#         max_length=3
#     )
#
#     famsup = models.CharField(
#         verbose_name="Suporte educacional da família",
#         max_length=3
#     )
#
#     paid = models.CharField(
#         verbose_name="Aulas extras pagas",
#         max_length=3
#     )
#
#     activities = models.CharField(
#         verbose_name="Atividades extracurriculares",
#         max_length=3
#     )
#
#     nursery = models.CharField(
#         verbose_name="Cursou creche",
#         max_length=3
#     )
#
#     higher = models.CharField(
#         verbose_name="Deseja cursar o ensino superior",
#         max_length=3
#     )
#
#     internet = models.CharField(
#         verbose_name="Acesso à internet em casa",
#         max_length=3
#     )
#
#     romantic = models.CharField(
#         verbose_name="Relacionamento romântico",
#         max_length=3
#     )
#
#     famrel = models.PositiveSmallIntegerField(
#         verbose_name="Qualidade das relações familiares",
#     )
#
#     freetime = models.PositiveSmallIntegerField(
#         verbose_name="Tempo livre depois da escola",
#     )
#
#     goout = models.PositiveSmallIntegerField(
#         verbose_name="Sair com os amigos",
#     )
#
#     dalc = models.PositiveSmallIntegerField(
#         verbose_name="Consumo de álcool no dia de trabalho",
#     )
#
#     walc = models.PositiveSmallIntegerField(
#         verbose_name="Consumo de álcool no fim de semana",
#     )
#
#     health = models.PositiveSmallIntegerField(
#         verbose_name="Estado de saúde atual",
#     )
#
#     absences = models.PositiveSmallIntegerField(
#         verbose_name="Número de faltas na escola",
#     )
#
#     g1 = models.PositiveSmallIntegerField(
#         verbose_name="Nota do primeiro período",
#     )
#
#     g2 = models.PositiveSmallIntegerField(
#         verbose_name="Nota do segundo período",
#     )
#
#     g3 = models.PositiveSmallIntegerField(
#         verbose_name="Nota do final",
#     )
#
#     horario_registro = models.DateTimeField(
#         verbose_name="Horário de registro",
#         auto_now_add=True
#     )
#
#     registrado_por = models.ForeignKey(
#         "docentes.Docente",
#         verbose_name="Docente responsável pelo registro",
#         on_delete=models.PROTECT
#     )
#
#     class Meta:
#         verbose_name = "Aluno"
#         verbose_name_plural = "Alunos"
#         db_table = "aluno"
#
#     def __str__(self):
#         return self.school
