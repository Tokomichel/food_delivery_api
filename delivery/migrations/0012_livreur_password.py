# Generated by Django 5.0.4 on 2024-05-04 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0011_alter_restaurant_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='livreur',
            name='password',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
