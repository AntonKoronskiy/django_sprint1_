from django.shortcuts import render
from django.template import loader


# Create your views here.
def about(request):
    #template = loader.get_template('pages/about.html')
    return render(request, 'pages/about.html')


def rules(request):
    #template = loader.get_template('pages/rules.html')
    return render(request, 'pages/rules.html')
