# Generated by Django 5.1.4 on 2024-12-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_age_min_alter_user_can_be_contacted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='can_be_contacted',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='data_can_be_shared',
            field=models.BooleanField(),
        ),
    ]
