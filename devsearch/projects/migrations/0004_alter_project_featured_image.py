# Generated by Django 4.1.3 on 2022-11-14 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='static/images/default.jpg', null=True, upload_to=''),
        ),
    ]
