# Generated by Django 5.0.2 on 2024-03-24 15:51

import django.db.models.deletion
import main.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=13, unique=True, validators=[main.validator.validate_phone_number])),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/products')),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.PositiveIntegerField()),
                ('product_description', models.TextField()),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categorymodel')),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ManyToManyField(to='main.productmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.usermodel')),
            ],
        ),
        migrations.CreateModel(
            name='HistoryOrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False)),
                ('is_cooking', models.BooleanField(default=False)),
                ('is_courier', models.BooleanField(default=False)),
                ('is_delivered', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.usermodel')),
            ],
        ),
    ]