# Generated by Django 3.2 on 2021-05-31 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoapp', '0006_alter_uploadfile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='images/videos/', verbose_name=''),
        ),
    ]
