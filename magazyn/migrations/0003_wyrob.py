# Generated by Django 2.1.7 on 2019-03-26 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazyn', '0002_auto_20190325_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wyrob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=200)),
                ('ilosc', models.IntegerField()),
            ],
        ),
    ]
