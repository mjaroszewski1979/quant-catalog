# Generated by Django 4.0.1 on 2022-01-20 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StrategyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('market', models.CharField(max_length=200)),
                ('cagr', models.DecimalField(decimal_places=2, max_digits=3)),
                ('sharpe', models.DecimalField(decimal_places=2, max_digits=3)),
                ('long_only', models.BooleanField()),
                ('description', models.TextField()),
            ],
        ),
    ]
