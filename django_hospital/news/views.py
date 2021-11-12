from django.shortcuts import render

# Create your views here.

def index(request):
    context = {

    }
     
    if request.method == "POST":
        print(request.POST)

    return render(request, 'home/index.html', context)