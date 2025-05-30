# Generated by Django 5.2 on 2025-05-06 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walk', '0013_goal'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='walk.goal')),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
    ]
