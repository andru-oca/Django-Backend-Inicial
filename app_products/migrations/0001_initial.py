# Generated by Django 4.2.7 on 2023-11-28 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('warehouse', models.CharField(choices=[('CL', 'Chile'), ('AR', 'Argentina'), ('CN', 'China'), ('PE', 'Peru'), ('PA', 'Panama'), ('CO', 'Colombia')], max_length=2)),
                ('code', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('expiration_date', models.DateField()),
                ('currency', models.CharField(choices=[('USD', 'US Dollars'), ('PES', 'Pesos'), ('REA', 'Reales'), ('EUR', 'Euros')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_products.product')),
            ],
        ),
    ]
