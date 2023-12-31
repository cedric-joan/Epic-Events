# Generated by Django 4.2.4 on 2023-08-28 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField()),
                ('last_name', models.CharField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField()),
                ('compagny_name', models.CharField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.FloatField(blank=True)),
                ('remaining_amount', models.FloatField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('contract_status', models.BooleanField(default=False, verbose_name='signed')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('event_date_start', models.DateTimeField()),
                ('event_date_end', models.DateTimeField()),
                ('location', models.CharField()),
                ('attendees', models.IntegerField()),
                ('notes', models.TextField(blank=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_client', to='events_app.client')),
                ('client_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_client', to='events_app.client')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='events_app.contract')),
            ],
        ),
    ]
