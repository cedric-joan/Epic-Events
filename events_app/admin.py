from django.contrib import admin

from events_app.models import Client, Contract, Event

admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Event)