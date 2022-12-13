# Generated by Django 4.1.1 on 2022-12-06 21:18

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('standard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adverts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.URLField(max_length=900)),
                ('short_description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='farming', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CommentProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('com_desc', models.TextField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('img_url', models.URLField(max_length=900)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('reached_in', models.DateTimeField(auto_now=True)),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_state', models.CharField(choices=[('ACCEPTED', 'Accepted'), ('DENIED', 'Denied'), ('SHIPPING', 'Shipped'), ('DELIVERED', 'Delivered')], default='Accepted', max_length=50)),
                ('Total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_quantity', models.PositiveIntegerField()),
                ('Created_in', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShopLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_email', models.EmailField(default=' ', max_length=254)),
                ('country', models.CharField(default=' ', max_length=100)),
                ('city', models.CharField(default=' ', max_length=100)),
                ('street_floor_apartment', models.CharField(default=' ', max_length=100)),
                ('postal_code', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_img_url', models.URLField(max_length=900)),
                ('commercial_registration', models.URLField(max_length=900)),
                ('user_img', models.URLField(max_length=900)),
                ('mobile_num', models.IntegerField()),
                ('verified', models.BooleanField()),
                ('shop_title', models.CharField(max_length=80)),
                ('shop_desc', models.TextField(max_length=1024)),
                ('shop_img_url', models.URLField(max_length=900)),
                ('vendor_joined_in', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendorComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('com_desc', models.TextField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('Commented_in', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='standard.vendor')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendorReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_desc', models.TextField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('comment_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='standard.vendorcomment')),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='standard.vendor')),
            ],
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='prod_quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='location',
            name='main_location',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='location',
            name='postal_code',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Short_desc',
            field=models.TextField(default=' ', max_length=500),
        ),
        migrations.AddField(
            model_name='product',
            name='permalink',
            field=models.URLField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price_type',
            field=models.CharField(choices=[('EGP', 'EGP'), ('USD', 'USD'), ('UR', 'UR')], default='EGP', max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='weight_type',
            field=models.CharField(choices=[('KILOGRAM', 'kg'), ('Gram', 'g'), ('TON', 'ton')], default='kg', max_length=10),
        ),
        migrations.AlterField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.AlterField(
            model_name='news',
            name='news_img_url',
            field=models.URLField(max_length=900),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_desc',
            field=models.TextField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_img_url',
            field=models.URLField(max_length=900),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
        migrations.AddField(
            model_name='shoplocation',
            name='vendor_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='standard.vendor'),
        ),
        migrations.AddField(
            model_name='adverts',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='standard.vendor'),
        ),
        migrations.AddField(
            model_name='product',
            name='in_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='standard.category'),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='standard.product'),
        ),
    ]