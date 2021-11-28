# Generated by Django 3.2.9 on 2021-11-29 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField(null=True)),
                ('image', models.ImageField(null=True, upload_to='movie/actors')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(max_length=100)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.actor')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField(null=True)),
                ('image', models.ImageField(null=True, upload_to='movie/directors')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=60)),
                ('image', models.ImageField(null=True, upload_to='movie/distributors')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(1, 'Poster'), (2, 'BackDrop')])),
                ('image', models.ImageField(null=True, upload_to='movie/images')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kobis_id', models.CharField(max_length=8)),
                ('tmdb_id', models.CharField(max_length=10)),
                ('imdb_id', models.CharField(max_length=10, null=True)),
                ('name', models.CharField(max_length=80)),
                ('running_time', models.IntegerField(null=True)),
                ('summary', models.TextField()),
                ('opening_date', models.DateField()),
                ('closing_date', models.DateField()),
                ('actors', models.ManyToManyField(through='movie.Character', to='movie.Actor')),
                ('directors', models.ManyToManyField(to='movie.Director')),
                ('distributors', models.ManyToManyField(to='movie.Distributor')),
                ('genres', models.ManyToManyField(to='movie.Genre')),
                ('images', models.ManyToManyField(related_name='_movie_movie_images_+', to='movie.Image')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie'),
        ),
    ]
