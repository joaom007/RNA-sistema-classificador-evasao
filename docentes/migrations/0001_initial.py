# Generated by Django 3.0 on 2021-05-24 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=194, verbose_name='Nome completo')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone de contato')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Docente',
                'verbose_name_plural': 'Docentes',
                'db_table': 'docente',
            },
        ),
    ]
