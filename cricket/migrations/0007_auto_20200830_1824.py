# Generated by Django 2.0 on 2020-08-30 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0006_auto_20200830_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='winner_team',
            field=models.ForeignKey(blank=True, db_column='cr_match_winner', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cr_match_winner', to='cricket.Team'),
        ),
    ]
