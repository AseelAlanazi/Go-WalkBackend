# Generated by Django 5.2 on 2025-05-05 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('walk', '0010_alter_goal_goal_alter_historicalgoal_goal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalgoal',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalgoal',
            name='user',
        ),
        migrations.DeleteModel(
            name='Goal',
        ),
        migrations.DeleteModel(
            name='HistoricalGoal',
        ),
    ]
