# Generated by Django 3.1.4 on 2021-01-15 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_others'),
    ]

    operations = [
        migrations.CreateModel(
            name='collegenotices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('date', models.DateField()),
                ('topic', models.CharField(max_length=100)),
                ('readmore', models.URLField(max_length=100)),
            ],
        ),
    ]
