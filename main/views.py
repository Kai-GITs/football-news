from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406360256',
        'name': 'Kalfin',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)