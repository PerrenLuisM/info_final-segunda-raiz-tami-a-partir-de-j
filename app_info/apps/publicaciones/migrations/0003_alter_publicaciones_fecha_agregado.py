# Generated by Django 4.2.2 on 2023-08-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaciones',
            name='fecha_agregado',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]