# Generated by Django 2.2.7 on 2020-01-17 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_userinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tui',
            options={'verbose_name': '是否推荐', 'verbose_name_plural': '是否推荐'},
        ),
        migrations.RemoveField(
            model_name='tui',
            name='name',
        ),
        migrations.AddField(
            model_name='tui',
            name='is_recommend',
            field=models.BooleanField(default=True, verbose_name='是否推荐'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tui',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Tui', verbose_name='是否推荐'),
        ),
    ]
