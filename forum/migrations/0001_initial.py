# Generated by Django 5.1.2 on 2024-10-09 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=50000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
