from django.contrib import admin

from website.models import Announcement, BoardMember, DjangoConEdition, GrantCycle, SponsoredEvent


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ["title", "published_at", "is_featured"]
    list_filter = ["is_featured"]
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"
    search_fields = ["title", "body"]


@admin.register(BoardMember)
class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ["name", "role", "is_current", "order"]
    list_editable = ["order", "is_current"]
    list_filter = ["is_current"]
    search_fields = ["name", "role"]


@admin.register(DjangoConEdition)
class DjangoConEditionAdmin(admin.ModelAdmin):
    list_display = ["year", "location", "start_date", "end_date", "status", "website_url"]
    list_filter = ["status"]
    ordering = ["-year"]


@admin.register(SponsoredEvent)
class SponsoredEventAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "event_date", "grant_amount", "is_published"]
    list_filter = ["is_published"]
    list_editable = ["is_published"]
    date_hierarchy = "event_date"
    search_fields = ["name", "organizer", "location"]


@admin.register(GrantCycle)
class GrantCycleAdmin(admin.ModelAdmin):
    list_display = ["__str__", "is_open", "max_amount", "deadline"]
