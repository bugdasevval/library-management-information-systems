# Generated by Django 5.0.2 on 2024-06-01 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lims_app', '0007_alter_book_cover_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
