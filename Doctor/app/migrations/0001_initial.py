# Generated by Django 2.2.5 on 2020-02-09 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('Short_descr', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=10000)),
            ],
        ),
    ]
