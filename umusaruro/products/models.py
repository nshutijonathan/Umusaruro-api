from django.db import models

# Create your models here.
class Products(models.Model):
    product_type=models.TextField(blank=False);
    product_category=models.TextField(blank=False);
    quantity_in_stock=models.PositiveIntegerField(default=0);
    supplier_name=models.TextField(blank=False);
    supplier_address=models.TextField(blank=False);
    supplier_contact=models.CharField(default='',max_length=20);
    added_on=models.DateField(auto_now=True);
    