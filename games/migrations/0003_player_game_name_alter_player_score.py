# Generated by Django 4.1 on 2022-09-05 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0002_playedgame"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="game_name",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="games.game"
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="score",
            field=models.IntegerField(null=True),
        ),
    ]