from datetime import datetime
from django.shortcuts import redirect
from django.contrib import messages
# from django.core.mail import send_mail
from .models import Contact


def contact(req):
    if req.method == 'POST':
        user_id = req.POST.get('user_id')
        realtor_email = req.POST.get('realtor_email')
        listing_id = req.POST.get('listing_id')
        listing = req.POST.get('listing')
        name = req.POST.get('name')
        email = req.POST.get('email')
        phone = req.POST.get('phone')
        message = req.POST.get('message')
        contact_date = datetime.now()

        exist = Contact.objects.all().filter(user_id__exact=user_id,
                                             listing_id__exact=listing_id).exists()
        if user_id != 0 and exist:
            messages.info(req, '''You have an existing inquery to this property. 
                            We\'ll notify the realtor to contact you ASAP.''')
        else:
            contact = Contact(listing=listing, listing_id=listing_id, name=name,
                              email=email, phone=phone, message=message,
                              contact_date=contact_date, user_id=user_id)
            contact.save()
            # ! UPDATE EMAIL SETTINGS within settings.py for send_mail to work
            # send_mail(
            #     subject=f'[BTRE] Inquiry on {listing}',
            #     message=f'An inquiry for {listing} with message:\n{message}',
            #     from_email='',
            #     recipient_list=[realtor_email],
            #     fail_silently=False
            # )
            messages.success(req, '''Your inquery is received. 
                            Realtor will contact you soon. Thank you.''')
        return redirect('listing', listing_id=listing_id)
    else:
        return redirect('listings')
