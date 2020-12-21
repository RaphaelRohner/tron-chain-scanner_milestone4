from django.shortcuts import render
import requests


# Create your views here.
def wallet_scanner(request):
    """ A view to check if Tronlink wallet is available in the browser. """

    context = {}

    return render(request, 'walletscanner/walletscanner.html', context)


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


get_transactions_trc20()
