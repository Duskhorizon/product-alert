# Generated by Django 2.1.7 on 2019-03-25 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazyn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'email',
            },
        ),
        migrations.AlterField(
            model_name='surowiec',
            name='ilosc',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='surowiec',
            name='minimum',
            field=models.FloatField(),
        ),
    ]
