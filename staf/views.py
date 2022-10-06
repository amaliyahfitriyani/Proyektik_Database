from django.shortcuts import render
from staf.models import Staf
# Create your views here.
def staf(request):
    context = {
        'staf': Staf.objects.all()

    }
    return render(request, "staf.html", context)
