# Generated by Django 2.0.1 on 2018-02-19 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClubBoard', '0002_auto_20180214_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_post',
            name='view_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='create_post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/%Y/%m/%d/', verbose_name='동아리 포스터'),
        ),
    ]