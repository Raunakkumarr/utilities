from django.contrib import admin
from notice_updates.models import subscription
# Register your models here.
@admin.register(subscription)
class Subscription(admin.ModelAdmin):
	list_display = ('emails', 'category')
	search_fields = ('emails', 'category')
