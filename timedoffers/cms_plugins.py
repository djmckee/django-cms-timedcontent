from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
import datetime
from .models import TimedOffer


class TimedOffersPlugin(CMSPluginBase):
    render_template = "timed_offers_plugin.html"

    def render(self, context, instance, placeholder):
        now = datetime.datetime.now()
        context['offers'] = TimedOffer.objects.filter(start_date__lt=now, end_date__gt=now)
        return context

plugin_pool.register_plugin(TimedOffersPlugin)
