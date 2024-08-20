# Generated by Django 4.2.4 on 2023-11-23 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estilista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('especialidad', models.CharField(max_length=50)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=30)),
                ('fono', models.CharField(max_length=20)),
                ('fecha', models.DateTimeField()),
                ('estilista', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=15)),
                ('observacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('correo', models.EmailField(max_length=70, unique=True)),
                ('usuario', models.CharField(max_length=50, unique=True)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('activo', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=False)),
                ('tecnico', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
