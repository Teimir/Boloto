# Generated by Django 4.2.3 on 2023-09-04 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_attachment_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.FileField(blank=True, upload_to='attachments/'),
        ),
    ]
