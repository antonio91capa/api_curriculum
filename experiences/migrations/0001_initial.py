# Generated by Django 5.0.7 on 2024-07-27 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ini', models.DateTimeField()),
                ('date_end', models.DateTimeField(null=True)),
                ('company', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'experiences',
            },
        ),
    ]