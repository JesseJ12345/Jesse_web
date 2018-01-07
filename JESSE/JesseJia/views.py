from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def blog(request):
    return render(request, 'blog.html')


def skeleton(request):
    return render(request, 'skeleton.html')

def aside(request):
    return render(request, 'aside.html')

def landing(request):
    return render(request, 'landing.html')

def inbox(request):
    return render(request, 'inbox.html')

def forum(request):
    return render(request, 'forum.html')

def hero(request):
    return render(request, 'hero.html')

def cover(request):
    return render(request, 'cover.html')

def admin(request):
    return render(request, 'admin.html')

