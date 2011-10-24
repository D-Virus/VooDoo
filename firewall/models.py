from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

PROTOCOL_CHOICES = (
    ('TCP', 'TCP'),
    ('UDP', 'UDP'),
    ('GRE', 'GRE'),
)

SOURCE_CHOICES = (
    ('mac_address', 'Direccion MAC]'),
    ('ip_address', 'Direccion IP'),
    ('network', 'Red'),
    ('ip_group', 'Grupos IP'),
    ('mac_group', 'Grupos MAC'),
)

RULE_STATUS_CHOICES = (
    ('enable', 'Activa'),
    ('disable', 'Inactiva'),
)


class OutgoingFirewall(models.Model):
    description = models.TextField()
    protocol = models.CharField(max_length=3, choices=PROTOCOL_CHOICES,
                                 default='tcp')
    network = models.CharField(max_length=30, choices=SOURCE_CHOICES,
                                default='ip_address')
    source_ip_address = models.CharField(max_length=39, blank=True)
    source_mac_address = models.CharField(max_length=17, blank=True)
    destination = models.CharField(max_length=39)
    destination_port = models.CharField(max_length=5)
    status = models.CharField(max_length=10, choices=RULE_STATUS_CHOICES,
                                default='Activa')

    def __unicode__(self):
        return u"-A OUTPUT -p %s -d %s - %s - %s" % (self.protocol,
        self.source_ip_address, self.destination, self.destination_port)


class IncomingFirewall(models.Model):
    description = models.TextField()
    protocol = models.CharField(max_length=3, choices=PROTOCOL_CHOICES,
                                 default='tcp')
    zone = models.CharField(max_length=30, choices=SOURCE_CHOICES,
                                default='ip_address')
    source_ip_address = models.CharField(max_length=39, blank=True)
    source_mac_address = models.CharField(max_length=17, blank=True)
    destination = models.CharField(max_length=39)
    destination_port = models.CharField(max_length=5)
    status = models.CharField(max_length=10, choices=RULE_STATUS_CHOICES,
                                default='Activa')

    def __unicode__(self):
        return u"-A INPUT -p %s - %s - %s - %s" % (self.protocol,
        self.source_ip_address, self.destination, self.destination_port)

class Zone(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=39)

    def __unicode__(self):
        return u" Zona %s - %s" % (self.name, self.address)


class FirewallAdmin(admin.ModelAdmin):
    # allow the admin to filter by status (by any of the choices)
    list_filter = ('status',)
    # instead of having "Ticket Object", the list display
    # will display these fields. Django doesn't care if it is an
    # actual field or a function
    list_display = ('id', 'protocol', 'network', 'source_ip_address',
    'destination', 'destination_port', 'status')
    # fields that django will search through when the admin
    # submits a search query.
    search_fields = ['description']


class ZoneAdmin(admin.ModelAdmin):
    pass


admin.site.register(OutgoingFirewall, FirewallAdmin, )
#admin.site.register(IncomingFirewall, FirewallAdmin, )
admin.site.register(Zone, ZoneAdmin, )
