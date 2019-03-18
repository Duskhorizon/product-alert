# Generated by Django 2.1.7 on 2019-03-18 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=200)),
                ('ilosc', models.IntegerField()),
                ('minimum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Surowiec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=200)),
                ('ilosc', models.DecimalField(decimal_places=2, max_digits=6)),
                ('minimum', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]