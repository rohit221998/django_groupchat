from django.contrib import admin
from .models import Room, Message

# Register your models here.
# admin.site.register(Room)
# admin.site.register(Message)
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display=['name', 'date']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display=['room', 'user' ,'date']