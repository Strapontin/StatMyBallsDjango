from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'StatMyBallsApi/home.html')


def create(request):
    return render(request, 'StatMyBallsApi/create.html')
