# Generated by Django 5.0.4 on 2024-05-24 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0015_alter_commande_client_alter_commande_livreur_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='livreur',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
