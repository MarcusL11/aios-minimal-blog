from django.shortcuts import render
from .models import Product, ProductImage
# Create your views here.


def product_list(request):
    products = Product.objects.all()
    products_with_images = []
    for product in products:
        front_image = product.images.filter(image_tag="front").first()
        products_with_images.append((product, front_image))

    context = {"products_with_images": products_with_images}
    return render(request, "products/product_list.html", context)
