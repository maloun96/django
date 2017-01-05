from django.shortcuts import render
def index(request):
    # The homepage of app
    context = {}
    return render(request, "shop/index.html", context)
