# Generated by Django 2.2.7 on 2020-01-19 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200117_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tui',
            field=models.BooleanField(default=True, verbose_name='是否推荐'),
        ),
        migrations.DeleteModel(
            name='Tui',
        ),
    ]
