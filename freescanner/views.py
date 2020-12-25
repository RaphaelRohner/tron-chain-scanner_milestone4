from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import requests

from .models import Identifiers
from .forms import FreescannerForm

from tronapi import Tron
from tronapi import HttpProvider


# Create your views here.
def freescanner(request):
    """
    A view to check if Tronlink wallet is available in the browser.
    """

    # url = "https://api.trongrid.io/v1/accounts/TTfoWGU2M939cgZm8CksPtz1ytJRM9GiN7"  # noqa: E501

    # response = requests.request("GET", url)

    # print(response.text)

    template = 'freescanner/freescanner.html/'

    context = {}

    return render(request, template, context)


def identifiers(request):
    """
    A view to add and edit identifier.
    """

    identifiers = Identifiers.objects.all()  # pylint: disable=maybe-no-member

    if request.method == 'POST':
        form = FreescannerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Identifier added successfully')
            response = redirect('/freescanner/add/')
            return response
        else:
            messages.error(request, 'Action failed. Please ensure the form is valid.')  # noqa: 501
    else:
        form = FreescannerForm()

    template = 'freescanner/add_identifier.html/'
    context = {
        'form': form,
        'identifiers': identifiers,
    }

    return render(request, template, context)


def edit_identifier(request, item_id):
    """ A view to edit a identifier stored in the database """

    # get the clicked identifier belonging to the link clicked
    identifier = get_object_or_404(Identifiers, pk=item_id)
    print(identifier.id, identifier.identifier_name)

    # handle form submissions
    if request.method == 'POST':
        form = FreescannerForm(request.POST, request.FILES, instance=identifier)  # noqa: E501
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated identifier!')
            response = redirect('/freescanner/add/')
            return response
        else:
            messages.error(request, 'Failed to update identifier. Please ensure the form is valid.')  # noqa: E501
    else:
        form = FreescannerForm(instance=identifier)
        messages.info(request, f'You are editing {identifier.identifier_name}')  # noqa: E501

    # render the template
    template = 'freescanner/edit_identifier.html/'
    context = {
        'form': form,
        'identifier': identifier,
    }

    print(context)

    return render(request, template, context)


def delete_identifier(request, item_id):
    identifier = get_object_or_404(Identifiers, pk=item_id)
    identifier.delete()
    messages.success(request, 'Identifier deleted!')
    response = redirect('/freescanner/add/')
    return response


full_node = HttpProvider('https://api.trongrid.io')
solidity_node = HttpProvider('https://api.trongrid.io')
event_server = HttpProvider('https://api.trongrid.io')
tron = Tron(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)


# TRON API OPTIONS FOR TRC10 TOKENS
def get_trc10_tokens():
    """ A view to receive all trc10 tokens """

    url = "https://api.trongrid.io/v1/assets"

    response = requests.request("GET", url)

    print(response.text)


def get_token_by_name():
    """ A view to receive all trc10 tokens """

    token = "DIGIKEY"

    url = "https://api.trongrid.io/v1/assets/{}/list".format(token)

    response = requests.request("GET", url)

    print(response.text)


def get_token_by_id():
    """ A view to receive a trc10 token by its ID """

    identifier = "1003563"  # DIGIKEY

    url = "https://api.trongrid.io/v1/assets/{}".format(identifier)

    response = requests.request("GET", url)

    print(response.text)


# TRON API OPTIONS VIA CONTRACTS
def get_contract():
    """ A view to receive a contract by its ID """

    contract = tron.address.to_hex('TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7')  # noqa: E501 WINK

    print(contract)

    url = "https://api.trongrid.io/v1/contracts/{}/transactions".format(contract)  # noqa: E501

    response = requests.request("GET", url)

    print(response.text)


def get_token_balances():
    """ A view to receive the token balance of a contract """

    contract = tron.address.to_hex('TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7')  # noqa: E501 WINK

    print(contract)

    url = "https://api.trongrid.io/v1/contracts/{}/tokens".format(contract)  # noqa: E501

    response = requests.request("GET", url)

    print(response.text)


# TRON API OPTIONS VIA EVENTS
def get_event_by_id():
    """ A view to receive an event by its ID """

    event = "74684615f1f09e334ea2ca806f0dc74c1053ff237435165c87a1f22e86dc0697"  # noqa: E501

    print(event)

    url = "https://api.trongrid.io/v1/transactions/{}/events".format(event)  # noqa: E501

    response = requests.request("GET", url)

    print(response.text)


def get_events_by_contract():
    """ A view to receive events by of a contract """

    contract = "TE3L3rqrPrYh59FpvYPAHg6YpMR7qCpJ9m"

    print(contract)

    url = "https://api.trongrid.io/v1/contracts/{}/events".format(contract)  # noqa: E501

    response = requests.request("GET", url)

    print(response.text)


def get_events_by_block():
    """ A view to receive events of a block """

    block = "26068354"

    print(block)

    url = "https://api.trongrid.io/v1/blocks/{}/events".format(block)  # noqa: E501

    response = requests.request("GET", url)

    print(response.text)


def get_latest_block_events():
    """ A view to receive the latest block events """

    url = "https://api.trongrid.io/v1/blocks/latest/events"

    response = requests.request("GET", url)

    print(response.text)
