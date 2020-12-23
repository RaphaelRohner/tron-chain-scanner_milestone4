from django.shortcuts import render
from django.contrib import messages
import requests

from .models import Wallet
from .forms import WalletForm


# Create your views here.
def wallet_scanner(request):
    """ A view to check if Tronlink wallet is available in the browser. """

    userwallet = request.POST.get('tronlink')
    print(userwallet)

    context = {}

    return render(request, 'walletscanner/walletscanner.html', context)


def mwallet(request):
    """
    A view to add a main wallet.
    """

    wallet = Wallet.objects.all()  # pylint: disable=maybe-no-member

    if request.method == 'POST':
        form = WalletForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wallet added successfully')
        else:
            messages.error(request, 'Action failed. Please ensure the form is valid.')  # noqa: 501
    else:
        form = WalletForm()

    template = 'walletscanner/edit_primary_wallet.html'
    context = {
        'form': form,
        'wallet': wallet,
    }

    return render(request, template, context)


# TRON API OPTIONS VIA ACCOUNT
def get_account():
    """ A view to receive infos for a specific wallet address """

    wallet = "TTfoWGU2M939cgZm8CksPtz1ytJRM9GiN7"

    url = "https://api.trongrid.io/v1/accounts/{}".format(wallet)

    print(url)

    response = requests.request("GET", url)

    print(response.text)


def get_transactions():
    """ A view to receive transactions of a specific wallet address """

    wallet = "TTfoWGU2M939cgZm8CksPtz1ytJRM9GiN7"

    url = "https://api.trongrid.io/v1/accounts/{}/transactions".format(wallet)

    response = requests.request("GET", url)

    print(response.text)


def get_transactions_trc20():
    """ A view to receive trc20 transactions of a specific wallet address """

    wallet = "TTfoWGU2M939cgZm8CksPtz1ytJRM9GiN7"

    url = "https://api.trongrid.io/v1/accounts/{}/transactions/trc20".format(wallet)  # noqa: E501

    response = requests.request("GET", url)

    print(response.text)
