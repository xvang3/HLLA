# Generated by Django 5.1.2 on 2024-11-11 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_word_english_word_alter_word_hmong_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='image_filename',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
