# Generated by Django 5.0.2 on 2024-06-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lims_app', '0010_remove_book_title_book_image_book_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
                ('publish_date', models.DateField()),
                ('page_count', models.IntegerField()),
                ('book_code', models.CharField(max_length=100)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='book_covers/')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
