# Generated by Django 4.0.1 on 2022-01-27 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_market_strategy_delete_strategylist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='market',
            options={'verbose_name': 'market', 'verbose_name_plural': 'markets'},
        ),
        migrations.AlterModelOptions(
            name='strategy',
            options={'verbose_name': 'strategy', 'verbose_name_plural': 'strategies'},
        ),
    ]
