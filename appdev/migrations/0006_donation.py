# Generated by Django 3.2.6 on 2021-11-30 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdev', '0005_remove_exclusivevoucher_ev_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('mop', models.CharField(max_length=30)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
