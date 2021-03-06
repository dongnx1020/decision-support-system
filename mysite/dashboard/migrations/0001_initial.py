# Generated by Django 3.0.5 on 2020-04-26 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClusterCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink', models.FloatField()),
                ('rice', models.FloatField()),
                ('spice', models.FloatField()),
                ('conv', models.FloatField()),
                ('fruit', models.FloatField()),
                ('other', models.FloatField()),
                ('nonfood', models.FloatField()),
                ('veget', models.FloatField()),
                ('meat', models.FloatField()),
                ('fish', models.FloatField()),
                ('tea', models.FloatField()),
                ('count', models.FloatField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TotalMoneyCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink', models.FloatField()),
                ('rice', models.FloatField()),
                ('spice', models.FloatField()),
                ('conv', models.FloatField()),
                ('fruit', models.FloatField()),
                ('other', models.FloatField()),
                ('nonfood', models.FloatField()),
                ('veget', models.FloatField()),
                ('meat', models.FloatField()),
                ('fish', models.FloatField()),
                ('tea', models.FloatField()),
                ('count', models.FloatField()),
                ('date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='ClusterCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.ClusterCenter')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Customer')),
            ],
        ),
    ]
