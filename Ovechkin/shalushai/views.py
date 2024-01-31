from django.shortcuts import render
def index(request):
    """Переодресация"""

    return render(request, 'salupon/index.html')
def in_log(request):
    """Переодресация"""

    return render(request, 'salupon/in_log_index.html')

def settings(request):
    """Переодресация"""

    return render(request, 'salupon/settings.html')

# Create your views here.
