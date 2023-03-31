from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class CategoryModel(TimeStampedModel):
    category_name = models.CharField(max_length=150)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.category_name   
                                     

class ProductModel(TimeStampedModel):
    product_name = models.CharField(max_length=150)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.FileField(upload_to='images/product/')
    CategoryModel=models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Order(TimeStampedModel):
    customername = models.CharField(max_length=180)
    customeremail = models.EmailField(max_length=250)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


   
    

class CustomerOrder(TimeStampedModel):
    cname = models.CharField(max_length=180)
    cemail = models.EmailField(max_length=250)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()