# Generated by Django 3.1.7 on 2021-09-16 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedbackdata',
            old_name='rating',
            new_name='ramnaamjap',
        ),
        migrations.RemoveField(
            model_name='feedbackdata',
            name='feedback',
        ),
    ]
