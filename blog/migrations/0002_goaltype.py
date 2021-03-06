# Generated by Django 3.0.5 on 2020-04-13 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_objective', models.CharField(blank=True, max_length=300)),
                ('goal_choice_type', models.CharField(blank=True, choices=[('Savings', 'Savings'), ('Expenses', 'Expenses'), ('Debt', 'Debt')], max_length=30, null=True)),
                ('goal_accomplished', models.BooleanField()),
            ],
        ),
    ]
