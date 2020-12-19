from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from profiles.models import UserProfile  # import the user's profile
from .models import UserAddresses
from .forms import UserAddressesForm


@login_required
def address(request):
    """ \
    Display address form and list of user's addresses. \
    Add a new address. \
    """
    # profile = get_object_or_404(UserProfile, user=request.user)
    addresses = UserAddresses.objects.filter(user=request.user)  # noqa: E501, pylint: disable=maybe-no-member

    if request.method == 'POST':
        form = UserAddressesForm(request.POST,
                                 instance=UserAddresses(user=request.user))
        if form.is_valid():
            form.save()
            messages.success(request, 'Address added successfully')
        else:
            messages.error(request, 'Action failed. Please ensure the form is valid.')  # noqa: 501
    else:
        form = UserAddressesForm()

    template = 'user_addresses/addresses.html'
    context = {
        'form': form,
        'addresses': addresses,
    }

    return render(request, template, context)


@login_required
def edit_address(request, item_id):
    """ Edit an user address in the profile """

    # catch manual entered edit address urls
    # and check if address belongs to user
    currentUser = request.user
    address = get_object_or_404(UserAddresses, pk=item_id)
    addressOwner = address.user

    if not currentUser == addressOwner:
        messages.error(request, 'You can only edit your own addresses.')
        response = redirect('/address/')
        return response

    # handle form submissions
    if request.method == 'POST':
        form = UserAddressesForm(request.POST, request.FILES, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated address!')
            response = redirect('/address/')
            return response
        else:
            messages.error(request, 'Failed to update address. Please ensure the form is valid.')  # noqa: E501
    else:
        form = UserAddressesForm(instance=address)
        messages.info(request, f'You are editing {address.additional_full_name}')  # noqa: E501

    # render the template
    template = 'user_addresses/edit_addresses.html'
    context = {
        'form': form,
        'address': address,
    }

    return render(request, template, context)


@login_required
def delete_address(request, item_id):
    address = get_object_or_404(UserAddresses, pk=item_id)
    address.delete()
    messages.success(request, 'Address deleted!')
    response = redirect('/address/')
    return response
