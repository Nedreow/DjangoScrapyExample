# Generated by Django 4.2.4 on 2023-08-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0003_alter_scrapingsandbox_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapingsandbox',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='scrapingsandbox',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scrapingsandbox',
            name='source_url',
            field=models.URLField(max_length=100),
        ),
    ]