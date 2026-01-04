from django.contrib import admin
from .models import SiteSettings, Education, Skill


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    
    def has_add_permission(self, request):
        # Only allow one settings object
        return not SiteSettings.objects.exists()


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_year', 'end_year', 'order')
    list_editable = ('order',)
    list_filter = ('start_year',)
    search_fields = ('degree', 'institution', 'field_of_study')
    ordering = ('-start_year', 'order')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'order')
    list_editable = ('order', 'proficiency')
    list_filter = ('category',)
    search_fields = ('name',)