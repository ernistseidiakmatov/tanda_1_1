# Generated by Django 5.0.1 on 2024-01-06 11:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('search', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoomTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_playing', models.BooleanField(default=False)),
                ('vote', models.IntegerField(default=0)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.room')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.track')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='tracks',
            field=models.ManyToManyField(through='player.RoomTrack', to='search.track'),
        ),
    ]
