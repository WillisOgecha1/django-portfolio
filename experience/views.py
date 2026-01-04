from django.shortcuts import render
from .models import Experience, Certification


def experience_list(request):
    experiences = Experience.objects.all()
    certifications = Certification.objects.all()
    
    return render(
        request,
        "experience/experience.html",
        {
            "experiences": experiences,
            "certifications": certifications,
        },
    )