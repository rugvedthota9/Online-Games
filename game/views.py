from django.shortcuts import render


def game(request):
    return render(request, 'Home.html')


def privacy(request):
    return render(request, 'Privacy Policy.html')


def rules(request):
    return render(request, 'rules.html')


def about(request):
    return render(request, 'about.html')