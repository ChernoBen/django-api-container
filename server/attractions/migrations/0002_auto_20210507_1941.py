# Generated by Django 3.2.2 on 2021-05-07 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attractions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=200)),
                ('duration', models.TextField()),
                ('min_age', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
