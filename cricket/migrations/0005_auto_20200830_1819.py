# Generated by Django 2.0 on 2020-08-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0004_auto_20200830_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='schedule_date',
            field=models.DateField(db_column='CG_URM_MODIFICATION_DT', null=True),
        ),
    ]
