# Generated by Django 4.1 on 2022-10-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='userImage',
            field=models.ImageField(blank=True, null=True, upload_to='userImage/'),
        ),
    ]
