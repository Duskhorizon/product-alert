# Generated by Django 2.1.7 on 2019-04-02 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazyn', '0003_wyrob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transakcja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kto', models.CharField(max_length=200)),
                ('co', models.CharField(max_length=200)),
                ('ile', models.CharField(max_length=200)),
                ('kiedy', models.DateTimeField()),
            ],
        ),
    ]
