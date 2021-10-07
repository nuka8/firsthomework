from django.shortcuts import render


def index(request):
    name = 'Sultanbek Murat'
    return render(request, 'index.html', locals())