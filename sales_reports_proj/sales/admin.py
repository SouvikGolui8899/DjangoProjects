from django.contrib import admin

from sales.models import CSV, Position, Sale

# Register your models here.
admin.site.register(Position)
admin.site.register(Sale)
admin.site.register(CSV)
