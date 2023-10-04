# Generated by Django 4.0.3 on 2023-10-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('read', 'read'), ('wishlist', 'wishlist')], max_length=50)),
                ('published_on', models.DateField(null=True)),
                ('cover_image', models.URLField(null=True)),
                ('rating', models.FloatField(null=True)),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
    ]