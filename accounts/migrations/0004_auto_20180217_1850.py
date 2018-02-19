# Generated by Django 2.0.1 on 2018-02-17 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClubBoard', '0002_auto_20180214_2117'),
        ('InformationBoard', '0002_auto_20180214_2117'),
        ('PlanningBoard', '0021_auto_20180215_1419'),
        ('accounts', '0003_auto_20180202_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='like_club',
            field=models.ManyToManyField(to='ClubBoard.Create_Post'),
        ),
        migrations.AddField(
            model_name='profile',
            name='like_info',
            field=models.ManyToManyField(to='InformationBoard.Info_Article'),
        ),
        migrations.AddField(
            model_name='profile',
            name='like_planning',
            field=models.ManyToManyField(to='PlanningBoard.Planning'),
        ),
    ]