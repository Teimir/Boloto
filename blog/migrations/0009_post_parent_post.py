# Generated by Django 4.2.4 on 2024-06-02 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_data_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='parent_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_comments', to='blog.post'),
        ),
    ]
