from django.db import models
from users.models import User



class Client(models.Model):

    first_name = models.CharField()
    last_name = models.CharField()
    email = models.EmailField()
    phone_number = models.CharField()
    compagny_name = models.CharField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="clients")

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.compagny_name} - contact: {self.sales_contact.username}"


class Contract(models.Model):

    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="contract_client")
    sales_contact_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contract_sailor")
    total_amount = models.FloatField(blank=True)
    remaining_amount = models.FloatField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    contract_status = models.BooleanField(verbose_name="signed", default=False)

    def __str__(self):
        return f"Contrat:{self.id} - Client:{self.client.id}{self.client.last_name} - Contact:{self.sales_contact.username}"


class Event(models.Model):

    title = models.CharField(null=False)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name="event")
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="event_client")
    client_contact_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="email_client")
    event_date_start = models.DateTimeField()
    event_date_end = models.DateTimeField()
    support_contact_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_support")
    location = models.CharField()
    attendees = models.IntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Contrat:{self.contract.id} - Client:{self.client.last_name} - Contact:{self.support_contact.username}"
    