from django.http import HttpResponse
from django.template import loader
from .models import Featured_Product

# Create your views here.
def main(request):
    featuredProduct = Featured_Product.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'featuredProduct': featuredProduct,
    }
    return HttpResponse(template.render(context, request))