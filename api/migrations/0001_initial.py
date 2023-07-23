# Generated by Django 4.1 on 2023-07-23 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id_no', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, default='blogImage/default.png', null=True, upload_to='blogImage/')),
                ('content', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('likeNo', models.IntegerField(default=0)),
                ('commentNo', models.IntegerField(default=0)),
                ('created', models.DateField(auto_now_add=True)),
                ('seo_tags', models.CharField(blank=True, max_length=1000, null=True)),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='Author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('idName', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='', max_length=50)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id_no', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=1000)),
                ('subject', models.CharField(max_length=1000)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id_no', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('comment', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('master', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.comment')),
                ('parentBlog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.blog')),
                ('uploader', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='BlogCategory', to='api.category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='Likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
