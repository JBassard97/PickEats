from django.shortcuts import render

def simple_view(request):
    return render(request, "menuApp/simple_view.html")