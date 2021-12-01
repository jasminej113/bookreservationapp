from django.contrib import admin

from reservation.models import studentdetails
from reservation.models import bookdetails
from reservation.models import bookreservation
# Register your models here.

admin.site.register(studentdetails)
admin.site.register(bookdetails)
admin.site.register(bookreservation)