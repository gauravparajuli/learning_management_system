# Generated by Django 4.2.8 on 2023-12-09 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursecategory',
            options={'verbose_name_plural': 'course categories'},
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='qualificaton',
            new_name='qualification',
        ),
    ]
