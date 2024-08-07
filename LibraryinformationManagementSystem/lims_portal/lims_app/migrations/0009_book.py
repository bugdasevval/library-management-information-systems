# Generated by Django 5.0.2 on 2024-06-01 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lims_app', '0008_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
                ('publish_date', models.DateField()),
            ],
        ),
    ]
