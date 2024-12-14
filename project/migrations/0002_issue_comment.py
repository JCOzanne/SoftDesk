# Generated by Django 5.1.4 on 2024-12-14 11:26

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1000)),
                ('priority', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], max_length=10, verbose_name='Type')),
                ('tag', models.CharField(choices=[('BUG', 'Bug'), ('FEATURE', 'Feature'), ('TASK', 'Task')], max_length=10, verbose_name='Type')),
                ('status', models.CharField(choices=[('TODO', 'Todo'), ('IN_PROGRESS', 'In Progress'), ('FINISHED', 'Finished')], max_length=20, verbose_name='Type')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('in_charge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_charge', to='project.contributor')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='project.project')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('description', models.CharField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='project.issue')),
            ],
        ),
    ]
