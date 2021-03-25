# Generated by Django 3.1.7 on 2021-03-25 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StatMyBallsApi', '0005_goal_goal_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StatMyBallsApi.contest')),
            ],
        ),
        migrations.CreateModel(
            name='TeamColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rgb_value', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TeamComposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StatMyBallsApi.player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StatMyBallsApi.team')),
            ],
        ),
        migrations.RemoveField(
            model_name='goal',
            name='player_position',
        ),
        migrations.AddField(
            model_name='goaltype',
            name='is_from_defense',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PlayerPosition',
        ),
        migrations.AddField(
            model_name='team',
            name='team_color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StatMyBallsApi.teamcolor'),
        ),
        migrations.AddField(
            model_name='goal',
            name='contest',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='StatMyBallsApi.contest'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goal',
            name='enemy_player',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='goal_enemy_player', to='StatMyBallsApi.player'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goal',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal_player_scored', to='StatMyBallsApi.player'),
        ),
    ]
