from django.shortcuts import render

# Create your views here.


def dashboard(request):
    context = {}

    return render(request, 'dashboard.html', context)

def formtest(request):
    context = {}
    return render(request, 'form.html', context)
