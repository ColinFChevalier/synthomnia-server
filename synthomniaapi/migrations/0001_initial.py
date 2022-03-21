# Generated by Django 4.0.3 on 2022-03-08 03:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=500)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('imgURL', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Track has not been named', max_length=50)),
                ('bandcampURL', models.CharField(max_length=1000)),
                ('artistId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synthomniaapi.artist')),
                ('moodId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synthomniaapi.mood')),
            ],
        ),
        migrations.CreateModel(
            name='SynthomniaUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(default='I have not created a bio yet', max_length=150)),
                ('profile_image_url', models.URLField(max_length=500, null=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('is_artist', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_moods', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='synthomniaapi.mood')),
            ],
        ),
    ]
