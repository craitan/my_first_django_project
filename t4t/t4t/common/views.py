from django.shortcuts import render


def index(reqeust):
    context = {}
    return render(reqeust, 'common/home-page.html', context)
