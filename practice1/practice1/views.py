from django.shortcuts import render

# Create your views here.

def index_view(request):
    context = {
        "current_user": request.user
    }
    return render(request, 'base.html', context)