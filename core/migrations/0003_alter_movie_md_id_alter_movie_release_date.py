# Generated by Django 5.2.1 on 2025-06-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_tmdb_id_movie_md_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='md_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
