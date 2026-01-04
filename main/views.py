from django.shortcuts import render
from .models import SiteSettings, Education, Skill


def home(request):
    settings = SiteSettings.objects.first()
    skills = Skill.objects.all()
    
    # Group skills by category
    skills_by_category = {}
    for skill in skills:
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)
    
    return render(request, 'main/home.html', {
        'settings': settings,
        'skills_by_category': skills_by_category,
    })


def contact(request):
    return render(request, 'main/contact.html')


def education(request):
    educations = Education.objects.all()
    return render(request, 'main/education.html', {
        'educations': educations
    })