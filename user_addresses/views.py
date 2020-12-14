from django.shortcuts import render


def address(request):
    """ Display the user's addresses. """

    template = 'addresses/addresses.html'
    context = {}

    return render(request, template, context)
