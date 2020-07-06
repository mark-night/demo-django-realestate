from django.shortcuts import render


def index(req):
    return render(req, 'pages/index.html', {'req': req})


def about(req):
    return render(req, 'pages/about.html', {'req': req})
