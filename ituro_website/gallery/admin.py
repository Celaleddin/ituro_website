from django.contrib import admin
from gallery.models import Gallery, Photo


class PhotoInlineAdmin(admin.TabularInline):
    model = Photo
    extra = 1


class GalleryAdmin(admin.ModelAdmin):
    exclude = ["created_at","slug"]
    list_display = ["title", "created_at"]
    list_filter = ["title"]
    inlines = [PhotoInlineAdmin]


admin.site.register(Gallery, GalleryAdmin)
