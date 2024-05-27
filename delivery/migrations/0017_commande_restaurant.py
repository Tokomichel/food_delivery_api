# Generated by Django 5.0.4 on 2024-05-24 23:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0016_alter_commande_livreur'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='commandes', to='delivery.restaurant'),
            preserve_default=False,
        ),
    ]
