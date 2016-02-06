from django.contrib import admin
from post.models import CommonEntry,NewsEntry,CategoryEntry,LinkEntry, \
    GalleryEntry, TeamEntry, SponsorEntry


class CommonEntryInlineAdmin(admin.TabularInline):
    model = CommonEntry
    extra = 1


class CategoryEntryInlineAdmin(admin.TabularInline):
    model = CategoryEntry
    extra = 1


class NewsEntryInlineAdmin(admin.TabularInline):
    model = NewsEntry
    exclude = ["slug"]
    extra = 1


class LinkEntryInlineAdmin(admin.TabularInline):
    model = LinkEntry
    extra = 1


class TeamEntryInlineAdmin(admin.TabularInline):
    model = TeamEntry
    extra = 1


class GalleryEntryInlineAdmin(admin.TabularInline):
    model = GalleryEntry
    extra = 1


class SponsorEntryInlineAdmin(admin.TabularInline):
    model = SponsorEntry
    exclude = ["created_at"]
    extra = 1
