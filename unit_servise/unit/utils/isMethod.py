from django.http import HttpResponse


def isMethod(request, func, method):
    if request.method == method:
        func(request)
    else:
        return HttpResponse("Incorrect Request", status=400, reason="Incorrect Request")