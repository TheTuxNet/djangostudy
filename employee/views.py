from django.http import HttpResponse


def index(request):
    # ... some code to handle the year
    data = 'Empl.Index'
    return HttpResponse(data)


def view(request, myid):
    # ... some code to handle the year
    data = 'Empl.View'
    return HttpResponse(data)
