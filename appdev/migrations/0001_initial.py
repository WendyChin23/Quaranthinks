# Generated by Django 3.2.6 on 2021-12-01 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountUser',
            fields=[
                ('uid', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('birthdate', models.DateField()),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=150)),
                ('message', models.TextField(null=True)),
            ],
        ),
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
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=20)),
                ('faculty_name', models.CharField(max_length=100)),
                ('units', models.FloatField()),
                ('midterm', models.FloatField()),
                ('finals', models.FloatField()),
                ('finalgrade', models.FloatField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdev.accountuser', to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralVoucher',
            fields=[
                ('gv_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('gv_code', models.IntegerField()),
                ('gv_title', models.CharField(max_length=20)),
                ('gv_percentage', models.CharField(max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdev.accountuser', to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='ExclusiveVoucher',
            fields=[
                ('ev_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ev_code', models.IntegerField()),
                ('ev_title', models.CharField(max_length=20)),
                ('ev_percentage', models.CharField(max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdev.accountuser', to_field='username')),
            ],
        ),
    ]
