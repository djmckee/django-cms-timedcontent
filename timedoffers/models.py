from cms.models.pluginmodel import CMSPlugin
from datetime import datetime, timedelta

from django.db import models


class TimedOffer(models.Model):
    heading = models.CharField(max_length=50, blank=False, default='Offer of the week', help_text='The heading that is to be shown above the offer (for example "Offer of the week")')
    offer_text = models.CharField(max_length=255, blank=False, help_text="Details about the offer")
    start_date = models.DateTimeField(blank=False, help_text="The date to start showing the offer at", default=datetime.now())
    end_date = models.DateTimeField(help_text="The date to stop showing the offer", blank=False, default=(datetime.now() + timedelta(days=7)))

    def __unicode__(self):
        return self.offer_text
