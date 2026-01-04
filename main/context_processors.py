from .models import SiteSettings


def site_settings(request):
    """Make site settings available to all templates"""
    settings = SiteSettings.objects.first()
    return {
        'site_settings': settings
    }