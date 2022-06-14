# Generated by Django 3.2 on 2021-04-25 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='İSİM')),
                ('subject', models.CharField(max_length=120, verbose_name='TELEFON')),
                ('email', models.CharField(max_length=120, verbose_name='E-MAİL')),
                ('phone', models.CharField(max_length=120, verbose_name='NOT')),
                ('message', models.TextField(max_length=120, verbose_name='NOT')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='phone',
            field=models.CharField(max_length=120, verbose_name='NOT'),
        ),
    ]