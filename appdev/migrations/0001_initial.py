# Generated by Django 3.2.6 on 2021-11-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idn', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('birthdate', models.DateField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
