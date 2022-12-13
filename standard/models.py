from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomerUser(models.Model):
    Userid = models.OneToOneField(User, on_delete=models.CASCADE)
    cust_img = models.ImageField(upload_to='customers', null=True, blank=True)
    description = models.CharField(max_length=100)


class Category(models.Model):
    category_name = models.CharField(max_length=100, default='farming')


class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    price_type = models.CharField(max_length=10, default="EGP")
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    weight_type = models.CharField(max_length=10, default="kg")
    prod_desc = models.TextField(max_length=1024)
    Short_desc = models.TextField(max_length=500, default=' ')
    created_in = models.DateTimeField(auto_now=True)
    prod_img = models.ImageField(upload_to='products', null=True, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    in_category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    quantity = models.PositiveIntegerField(default=1)


class News(models.Model):
    Title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    article = models.TextField()
    news_img = models.ImageField(upload_to='news', null=True, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Location(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street_floor_apartment = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    mobile_num = models.IntegerField()
    main_location = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])
    postal_code = models.CharField(max_length=50, null=True)


class CommentProduct(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    com_desc = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    prod_quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)


class ShopLocation(models.Model):
    shop_email = models.EmailField(max_length=254, default=' ')
    country = models.CharField(max_length=100, default=' ')
    city = models.CharField(max_length=100, default=' ')
    street_floor_apartment = models.CharField(max_length=100, default=' ')
    postal_code = models.CharField(max_length=50, null=True)


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identification_img = models.ImageField(upload_to='Ven_ID', null=True, blank=True)
    commercial_registration = models.ImageField(upload_to='Ven_com_register', null=True, blank=True)
    mobile_num = models.IntegerField()
    verified = models.BooleanField()
    shop_title = models.CharField(max_length=80)
    shop_desc = models.TextField(max_length=1024)
    shop_img = models.ImageField(upload_to='Shop_img', null=True, blank=True)
    vendor_joined_in = models.DateTimeField(auto_now=True)
    shoplocation = models.OneToOneField(ShopLocation, on_delete=models.CASCADE, default=1)


class VendorComment(models.Model):
    Commented_in = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    com_desc = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now=True)


class VendorReply(models.Model):
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    comment_id = models.OneToOneField(VendorComment, on_delete=models.CASCADE)
    com_desc = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    order_state = models.CharField(max_length=50)
    Total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_quantity = models.PositiveIntegerField()
    Created_in = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    prod_name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    prod_img_url = models.URLField(max_length=300, null=True)
    product_quantity = models.PositiveIntegerField()
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)


class Notification(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    reached_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AdvertsPro(models.Model):
    owner = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='ads', null=True, blank=True)
    short_description = models.CharField(max_length=500)
