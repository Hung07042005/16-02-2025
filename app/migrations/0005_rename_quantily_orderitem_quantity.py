# Generated by Django 5.1.6 on 2025-02-14 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_date_oder_order_date_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='quantily',
            new_name='quantity',
        ),
    ]
