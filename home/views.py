from django.shortcuts import render


# Create your views here.
def landing_page(request):
    return render(request, 'index.html')


def q_a(request):
    return render(request, 'home/q-a.html')


def terms(request):
    return render(request, 'home/terms-conditions.html')


def handler404(request, exception):
    """ Custom 404 page """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """ Custom 500 page """
    return render(request, "errors/500.html", status=500)


def handler403(request, exception):
    """ Custom 403 page """
    return render(request, "errors/403.html", status=403)


def handler405(request, exception):
    """ Custom 405 page """
    return render(request, "errors/405.html", status=405)
