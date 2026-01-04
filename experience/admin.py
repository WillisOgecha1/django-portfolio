from django.contrib import admin
from .models import Experience, Certification


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("year", "role", "organization", "order")
    list_editable = ("order",)
    list_filter = ("year",)
    search_fields = ("role", "organization", "skills")
    ordering = ("-year", "order")


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "issuer", "issue_date")
    list_filter = ("issuer", "issue_date")
    search_fields = ("name", "issuer")
    ordering = ("-issue_date",)