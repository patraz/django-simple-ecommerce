# Generated by Django 4.1.5 on 2023-02-01 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_rename_billing_adress_order_billing_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='primary_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='primary_category_products', to='cart.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='secondary_categories',
            field=models.ManyToManyField(related_name='secondary_category_products', to='cart.category'),
        ),
    ]
