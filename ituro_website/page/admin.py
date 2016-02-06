from django.contrib import admin
from post.admin import CommonEntryInlineAdmin, CategoryEntryInlineAdmin, \
    NewsEntryInlineAdmin, LinkEntryInlineAdmin, SponsorEntryInlineAdmin, \
    GalleryEntryInlineAdmin, TeamEntryInlineAdmin
from page.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "subject", "language_code", "is_public"]
    list_filter = ["title","language_code","is_public"]
    search_fields = ["title", "subject"]
    exclude = ["slug_title", "slug_subject", "created_at"]
    class Meta:
        abstract=True


class CommonPage(Page):
    class Meta:
        proxy=True


class CategoryPage(Page):
    class Meta:
        proxy=True


class HomePage(Page):
    class Meta:
        proxy=True


class GalleryPage(Page):
    class Meta:
        proxy=True


class SponsorPage(Page):
    class Meta:
        proxy=True


class TeamPage(Page):
    class Meta:
        proxy=True


class CommonPageAdmin(PageAdmin):
    inlines = [CommonEntryInlineAdmin,LinkEntryInlineAdmin]


class CategoryPageAdmin(PageAdmin):
    inlines = [CategoryEntryInlineAdmin]


class HomePageAdmin(PageAdmin):
    inlines = [NewsEntryInlineAdmin, LinkEntryInlineAdmin]


class TeamPageAdmin(PageAdmin):
    inlines = [TeamEntryInlineAdmin]


class GalleryPageAdmin(PageAdmin):
    inlines = [GalleryEntryInlineAdmin]


class SponsorPageAdmin(PageAdmin):
    inlines = [SponsorEntryInlineAdmin]


admin.site.register(CommonPage, CommonPageAdmin)
admin.site.register(CategoryPage, CategoryPageAdmin)
admin.site.register(HomePage, HomePageAdmin)
admin.site.register(TeamPage, TeamPageAdmin)
admin.site.register(GalleryPage, GalleryPageAdmin)
admin.site.register(SponsorPage, SponsorPageAdmin)
