# Generated by Django 2.0.1 on 2018-02-16 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PlanningBoard', '0020_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='planning',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='PlanningBoard.Planning'),
            preserve_default=False,
        ),
    ]