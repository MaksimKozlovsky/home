from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    value = request.GET.get('value')
    value_len = len(value)
    context = {
         'value': value,
         'value_len': value_len
               }
    return render(request, 'index.html', context=context)
# Create your views here.
