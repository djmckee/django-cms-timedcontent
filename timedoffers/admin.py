from django.contrib import admin
from .models import TimedOffer


class TimedOfferAdmin(admin.ModelAdmin):
    list_display = 'offer_text', 'start_date', 'end_date'
    search_fields = ['offer_text']

admin.site.register(TimedOffer, TimedOfferAdmin)
