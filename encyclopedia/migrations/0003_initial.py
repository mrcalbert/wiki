# Generated by Django 4.0.3 on 2022-03-25 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('encyclopedia', '0002_delete_searchlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='searchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
