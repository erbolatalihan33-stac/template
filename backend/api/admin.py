from django.contrib import admin

from .models import Note, Price, Profile, Service


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1


class PriceInline(admin.TabularInline):
    model = Price
    extra = 1


class NoteInline(admin.TabularInline):
    model = Note
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [ServiceInline, PriceInline, NoteInline]
    list_display = ("name", "age", "city", "status")
