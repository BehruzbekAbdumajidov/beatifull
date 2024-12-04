from django.shortcuts import render
from .models import Mahsulot, Rasm, Haridor, Mol


# Create your views here.
def index(request):
    mahsulot = Mahsulot.objects.all()
    rasm = Rasm.objects.all()
    haridor = Haridor.objects.all()
    mol = Mol.objects.all()



    context = {
        'mahsulot': mahsulot,
        'rasm': rasm,
        'haridor': haridor,
        'm': Mol
    }
    return render(request,'index.html', context=context)

def about(request):
    return render(request, 'about.html', context={})

def client(request):

    
    return render(request, 'client.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})

def products(request):

    mahsulot = Mahsulot.objects.all()

    context = {
        'mahsulot': mahsulot
    }
    return render(request, 'products.html', context=context)


def detail(request, pk):
    product = Mahsulot.objects.get(id=pk)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context=context)


