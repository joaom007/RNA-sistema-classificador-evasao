# Generated by Django 3.0 on 2021-09-20 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('docentes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_conclusao_anterior', models.PositiveSmallIntegerField(verbose_name='Ano de Conclusão do Ensino Anterior')),
                ('distancia_campus', models.FloatField(max_length=7, verbose_name='Distância do Câmpus (Km)')),
                ('nivel_ensino', models.CharField(max_length=20, verbose_name='Nível de Ensino')),
                ('periodo_atual', models.PositiveSmallIntegerField(verbose_name='Período Atual')),
                ('turno', models.CharField(max_length=15, verbose_name='Turno')),
                ('ano_previsao_conclusao', models.PositiveSmallIntegerField(verbose_name='Ano Letivo de Previsão de Conclusão')),
                ('codigo_curso', models.CharField(max_length=20, verbose_name='Código Curso')),
                ('ano_matricula', models.PositiveSmallIntegerField(verbose_name='Ano de Matrícula')),
                ('idade', models.PositiveSmallIntegerField(verbose_name='Idade')),
                ('etnia', models.CharField(max_length=20, verbose_name='Etnia/Raça')),
                ('frequencia', models.FloatField(max_length=5, verbose_name='Frequência no Período')),
                ('ira', models.FloatField(max_length=4, verbose_name='I.R.A.')),
                ('progresso', models.FloatField(max_length=5, verbose_name='Percentual de Progresso')),
                ('sexo', models.CharField(max_length=1, verbose_name='Sexo')),
                ('tipo_escola_origem', models.CharField(max_length=15, verbose_name='Tipo de Escola de Origem')),
                ('horario_registro', models.DateTimeField(auto_now_add=True, verbose_name='Horário de registro')),
                ('registrado_por', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='docentes.Docente', verbose_name='Docente responsável pelo registro')),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
                'db_table': 'aluno',
            },
        ),
    ]
