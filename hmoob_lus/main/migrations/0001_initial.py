# Generated by Django 5.1.2 on 2024-10-18 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alphabet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=255)),
                ('male_audio_file', models.FileField(blank=True, null=True, upload_to='audio/')),
                ('female_audio_file', models.FileField(blank=True, null=True, upload_to='audio/')),
                ('pronunciation_video_file', models.FileField(blank=True, null=True, upload_to='videos/')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_word', models.CharField(max_length=255)),
                ('hmong_word', models.CharField(max_length=255)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('male_audio_file', models.FileField(blank=True, null=True, upload_to='audio/')),
                ('female_audio_file', models.FileField(blank=True, null=True, upload_to='audio/')),
                ('pronunciation_video_file', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('real_video_file', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('animated_video_file', models.FileField(blank=True, null=True, upload_to='videos/')),
            ],
        ),
    ]
