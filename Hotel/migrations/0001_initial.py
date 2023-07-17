# Generated by Django 3.2.7 on 2021-10-09 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='imagecontainer')),
                ('desc', models.CharField(max_length=100)),
                ('FeeCancellation', models.BooleanField(default=True)),
                ('Total_Rooms', models.CharField(default=100, max_length=300)),
                ('Ratings', models.FloatField(blank=True, max_length=5)),
            ],
        ),
    ]
