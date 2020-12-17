from django.shortcuts import render


# Create your views here.
def free_scanner(request):
    """ A view to check if Tronlink wallet is available in the browser. """

    context = {}

    return render(request, 'freescanner/freescanner.html', context)
