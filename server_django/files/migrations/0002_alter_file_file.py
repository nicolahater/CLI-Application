# Generated by Django 4.0.4 on 2022-05-27 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/%Y/%m/%d/'),
        ),
    ]