# Generated by Django 3.0.8 on 2020-10-04 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='H:\\GitHub\\Pregunta-02\\Ruteo\\mediaimages/')),
            ],
        ),
    ]
