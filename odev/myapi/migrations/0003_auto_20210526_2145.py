# Generated by Django 3.2.3 on 2021-05-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_deneme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('operation_id', models.AutoField(primary_key=True, serialize=False)),
                ('operation_name', models.CharField(max_length=60)),
                ('product_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('order_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.PositiveIntegerField()),
                ('product_id', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.PositiveIntegerField()),
                ('order_date', models.DateField()),
                ('deadline', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=60)),
                ('product_type', models.CharField(max_length=50)),
                ('is_salable', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SubProductTree',
            fields=[
                ('sub_product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_id', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WorkCenterOperation',
            fields=[
                ('wc_opr_id', models.AutoField(primary_key=True, serialize=False)),
                ('work_center_id', models.PositiveIntegerField()),
                ('operation_id', models.PositiveIntegerField()),
                ('speed', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkCenters',
            fields=[
                ('work_center_id', models.AutoField(primary_key=True, serialize=False)),
                ('work_center_name', models.CharField(max_length=60)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Deneme',
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
    ]
