# Generated by Django 2.2.4 on 2019-10-27 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rollno',
            field=models.IntegerField(),
        ),
    ]
