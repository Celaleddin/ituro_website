from django.contrib import admin
from team.models import Team, TeamMember


class TeamMemberInlineAdmin(admin.TabularInline):
    model = TeamMember
    extra = 1


class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    exclude = ["created_at"]
    inlines = [TeamMemberInlineAdmin]


admin.site.register(Team, TeamAdmin)
