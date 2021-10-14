from django.http import HttpResponse as HP

def index(request):
    return HP("Hello,world.You're at the polls index.")
# Create your views here.
