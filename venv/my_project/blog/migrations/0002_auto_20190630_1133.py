# Generated by Django 2.2.2 on 2019-06-30 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='contents',
            new_name='content',
        ),
    ]
