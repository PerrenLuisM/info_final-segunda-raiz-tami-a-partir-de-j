# Generated by Django 4.2.2 on 2023-08-01 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0005_alter_comentarios_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='publicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='publicaciones.publicaciones'),
        ),
    ]
