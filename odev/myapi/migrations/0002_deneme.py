# Generated by Django 3.0.7 on 2021-05-26 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deneme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=60)),
                ('soyisim', models.CharField(max_length=60)),
            ],
        ),
    ]
