from django.contrib import admin
from .models import *
from .models import LoanDetail
from .models import Record
from .models import Bookso

admin.site.register(reader)
admin.site.register(LoanDetail)
admin.site.register(Record)
admin.site.register(Bookso)