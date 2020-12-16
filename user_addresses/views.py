from django.shortcuts import render  # , get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from profiles.models import UserProfile  # import the user's profile
from .models import UserAddresses
from .forms import UserAddressesForm


@login_required
def address(request):
    """ Display address form and the user's addresses. """
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

    template = 'addresses/addresses.html'
    context = {
        'form': form,
        'addresses': addresses,
    }

    return render(request, template, context)
