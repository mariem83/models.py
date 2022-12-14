# Generated by Django 4.1.1 on 2022-12-06 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0005_customeruser'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('prod_img_url', models.URLField(max_length=300, null=True)),
                ('product_quantity', models.PositiveIntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='standard.order')),
            ],
        ),
    ]
