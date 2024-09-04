from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306209933',
        'name': 'Naila Shakira Putrindari',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)