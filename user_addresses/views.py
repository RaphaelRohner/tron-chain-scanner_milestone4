from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile  # import the user's profile
from .models import UserAddresses
from .forms import UserAddressesForm


@login_required
def address(request):
    """ Display the user's addresses. """
    profile = get_object_or_404(UserProfile, user=request.user)
    addresses = UserAddresses.objects.all()
    # print(addresses)

    if request.method == 'POST':
        form = UserAddressesForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Address updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')  # noqa: 501
    else:
        form = UserAddressesForm()

    template = 'addresses/addresses.html'
    context = {
        'form': form,
        'addresses': addresses,
    }

    return render(request, template, context)
