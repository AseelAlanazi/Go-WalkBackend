# Generated by Django 5.2 on 2025-05-04 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('walk', '0008_reviewandcomments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewandcomments',
            old_name='rateing',
            new_name='rating',
        ),
    ]
