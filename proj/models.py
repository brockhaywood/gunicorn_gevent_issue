from django.db import models

class Context(models.Model):
    """
    Sport/League/GameType Contexts
    """
    context = models.CharField(max_length=10, unique=True, help_text="Sport/league/gametype context")
    name = models.CharField(max_length=255, help_text="Context name")

    class Meta:
        app_label = 'api'

    def __unicode__(self):
        return u'{0}'.format(self.context)


class Event(models.Model):

    name = models.CharField(max_length=255, help_text="Event Name")

    context = models.ForeignKey(
        Context, help_text="Context for this Event")

    description = models.CharField(
        max_length=255, null=True, blank=True, help_text="Event Description")

    scheduled_ts = models.DateTimeField(
        null=True,
        blank=True,
        help_text="When the event was scheduled to start replicating")

    open_ts = models.DateTimeField(
        help_text="When the event should start accepting tickets"
    )

    close_ts = models.DateTimeField(
        help_text="When the event should stop accepting tickets (live)")

    finalize_ts = models.DateTimeField(
        help_text="When the event should payout")

    commission = models.IntegerField(
        null=True, blank=True, default=0, help_text="Not in use")

    payout = models.IntegerField(
        null=True, blank=True,
        default=0, help_text="Total payout for this event")

    payout_currency = models.CharField(
        max_length=3, default="USD", help_text="Currency of payout")

    profit = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        help_text="Total profit for this event")

    paid_out = models.BooleanField(
        default=False, help_text="If the event has paid winners")

    ticket_min = models.IntegerField(
        default=0, help_text="Minimum of tickets for the event to run")

    ticket_max = models.IntegerField(
        default=0, help_text="Maximum of tickets allowed for this event")

    ticket_max_per_user = models.IntegerField(
        default=-1, help_text="Maximum of tickets allowed per entrant")

    ticket_cost = models.IntegerField(
        help_text="Cost for each ticket in cents")

    ticket_cost_currency = models.CharField(
        max_length=3, default="USD", help_text="Currency of Ticket Cost")

    selection_currency_allocation = models.IntegerField(
        help_text="The salary cap for outcome selections")

    serial = models.IntegerField(
        blank=True, null=True, help_text="Event sequence number")

    hidden = models.BooleanField(default=False)

    password = models.CharField(max_length=64, null=True, blank=True)

    settings_json = models.TextField(default="{}", help_text="JSON Settings")

    external_id = models.IntegerField(
        null=True, blank=True, help_text="Related statistics id")

    class Meta:
        app_label = 'api'
