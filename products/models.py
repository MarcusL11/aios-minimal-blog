from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    image_tag = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.product.name + " " + self.image_tag
