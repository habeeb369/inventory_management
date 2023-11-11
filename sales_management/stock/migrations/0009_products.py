# Generated by Django 4.2 on 2023-06-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_remove_pro_details_id_alter_pro_details_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
    ]
