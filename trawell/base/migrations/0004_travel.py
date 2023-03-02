# Generated by Django 4.1.6 on 2023-03-02 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_places_packages_places'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=55)),
                ('image', models.ImageField(upload_to='uploads/travels_image')),
            ],
        ),
    ]
