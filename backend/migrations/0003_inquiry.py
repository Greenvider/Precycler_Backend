# Generated by Django 4.2.6 on 2023-10-29 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_rename_store_stores'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=500)),
            ],
        ),
    ]
