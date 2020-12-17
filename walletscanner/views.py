from django.shortcuts import render


# Create your views here.
def wallet_scanner(request):
    """ A view to check if Tronlink wallet is available in the browser. """

    context = {}

    return render(request, 'walletscanner/walletscanner.html', context)
