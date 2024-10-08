from django.shortcuts import render

# Create your views here.


def home(requests):
    context = {
        'nav_links': [
            {'name': 'Home', 'url': 'home'},
            {'name': 'Service', 'url': 'service'},
        ]
    }
    return render(requests, 'home.html', context)


def service(requests):
    return render(requests,  'service.html')


def contact(requests):
    return render(requests, 'contact.html')
