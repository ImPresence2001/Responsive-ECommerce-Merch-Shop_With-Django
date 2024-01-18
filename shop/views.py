from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Featured_Product

# Create your views here.
def main(request):
    img = Featured_Product.objects.first()
    featuredProduct = Featured_Product.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'featuredProduct': featuredProduct,
        'img': img,
    }
    return HttpResponse(template.render(context, request))