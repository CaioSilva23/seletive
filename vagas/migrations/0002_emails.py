# Generated by Django 4.1.3 on 2022-11-23 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_vagas_email'),
        ('vagas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=100)),
                ('corpo', models.TextField()),
                ('enviado', models.BooleanField()),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='empresa.vagas')),
            ],
        ),
    ]
