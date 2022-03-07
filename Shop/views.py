from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Grocery
from .forms import Grocery_Form
# Create your views here.

def display(request):
    elements = Grocery.objects.all()
    return render(request,"display.html",{'Grocerry':elements})

def form_dis(request):
    if request.method == "POST":
        form = Grocery_Form(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['Name']
            RPU = form.cleaned_data['RatePerUnit']
            print(RPU)
            print("I PRINTED RPU")
            Quant = form.cleaned_data['Quantity']
            amount = Quant * RPU
            obj = Grocery.objects.filter(Name = name)
            if obj.exists():
                objs = Grocery.objects.get(Name = name)
                objs.Amount = amount
                objs.save()
            
            #post.Amount = amount
            #post.save()
            
            return render(request,"display.html",{'Type':amount})
            


    else:
        form = Grocery_Form()
        return render(request,"form.html",{'form':form})


            