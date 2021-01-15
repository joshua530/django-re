from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.post.get('id')
        listing = request.POST.get('listing')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        user_id = request.POST.get('user_id')

    if request.user.is_authenticated:
        user_id = request.user.id
        has_contacted = Contact.objects.filter(
            user_id=user_id, listing_id=listing_id)
        if has_contacted:
            messages.add_message(
                request, messages.ERROR, 'You have already made an enquiry for this listing')
            return redirect('listings', listing_id=listing_id)

    contact = Contact(listing=listing, listing_id=listing_id, name=name,
                      email=email, phone=phone, message=message, user_id=user_id)
    contact.save()
    messages.success(
        request, 'Your request has been submitted. A realtor will get back to you soon')
    return redirect('listings', listing_id=listing_id)
