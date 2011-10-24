from django.conf.urls.defaults import *
from models import OutgoingFirewall

info = {
    'queryset': OutgoingFirewall.objects.all(),
}

urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^$', 'object_list', info, name='outgoingfirewall-list'),
    url(R'^(?P<object_id>\d+)/$', 'object_detail', info, name='outgoingfirewall-detail'),
)

