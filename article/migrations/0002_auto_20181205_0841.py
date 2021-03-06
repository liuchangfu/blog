# Generated by Django 2.1.3 on 2018-12-05 00:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticelPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('slug', models.SlugField(max_length=500)),
                ('body', models.TextField(verbose_name='正文')),
                ('created', models.DateTimeField(default=datetime.datetime(2018, 12, 5, 0, 41, 18, 820316, tzinfo=utc), verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AlterModelOptions(
            name='articlecolumn',
            options={'verbose_name': '文章列表', 'verbose_name_plural': '文章列表'},
        ),
        migrations.AlterField(
            model_name='articlecolumn',
            name='column',
            field=models.CharField(max_length=200, verbose_name='列'),
        ),
        migrations.AlterField(
            model_name='articlecolumn',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='articlecolumn',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articel_column', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='articelpost',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_column', to='article.ArticleColumn', verbose_name='列'),
        ),
        migrations.AlterIndexTogether(
            name='articelpost',
            index_together={('id', 'slug')},
        ),
    ]
