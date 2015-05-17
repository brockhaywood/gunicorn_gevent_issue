from django.http import HttpResponse
import datetime
import models

def current_datetime(request):

    objects = models.Event.objects.all()

    print objects.count()

    lst = list(objects)

    print lst[0].context

    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)