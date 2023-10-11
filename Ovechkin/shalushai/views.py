from django.shortcuts import render
def index(request):
    """Переодресация"""

    return render(request, 'salupon/index.html')
# Create your views here.
