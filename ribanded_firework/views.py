from django.shortcuts import render
from .models import *

def index(request):
  products = Product.objects.all()
  context = {'products':products}
  return render(request, 'ribanded_firework/index.html', context)


#def madina(request):
 # return render(request, 'madina.html')
