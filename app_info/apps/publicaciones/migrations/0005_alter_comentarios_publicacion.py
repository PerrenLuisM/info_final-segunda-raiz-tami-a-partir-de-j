# Generated by Django 4.2.2 on 2023-08-01 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0004_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='publicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.publicaciones'),
        ),
    ]
