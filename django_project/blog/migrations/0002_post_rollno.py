# Generated by Django 2.2.4 on 2019-10-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rollno',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
