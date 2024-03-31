# Generated by Django 5.0.3 on 2024-03-30 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('descricao', models.CharField(max_length=500)),
                ('em_equipamento', models.BooleanField(default=True)),
                ('idade_minima_aluno', models.PositiveIntegerField(default=12)),
            ],
        ),
    ]
