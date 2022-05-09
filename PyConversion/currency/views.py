from django.shortcuts import render
from .models import Currency_convert_model
from .forms import Currency_form
from django.http import HttpResponse


def currency_function(request):
 
  if request.method == 'POST':
    form = Currency_form(request.POST)
    if form.is_valid():
      enter_amount = form.cleaned_data['amount']
      enter_choice = form.cleaned_data['convert_choice']
      with open('api.txt') as f:
          lines = f.readlines()
          currencyDict = {}
          for line in lines:
              parsed = line.split("\t")
              currencyDict[parsed[0]] = parsed[1] 
          if str(enter_choice) == "usd":  
            convert_amount = enter_amount * float(currencyDict[enter_choice])
            print(convert_amount) 
          else:
            form = Currency_form()
            convert_amount = enter_amount * float(currencyDict[enter_choice])
          return render(request,"currversion.html",{'form':form,'key':convert_amount})  
  else:
    form = Currency_form()
    # breakpoint()
  return render(request,"currversion.html",{'form':form})  
  