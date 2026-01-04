from django.db import models


class SiteSettings(models.Model):
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    name = models.CharField(max_length=100, default="Willis Ogecha")
    title = models.CharField(max_length=200, default="Machine Learning & Software Engineer")
    bio = models.TextField(default="I build intelligent, data-driven solutions using Machine Learning, Computer Vision, and modern backend technologies.")
    
    # CV/Resume
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True, help_text="Upload your CV/Resume (PDF)")
    
    # Social Media Links
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return "Site Settings"


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10, blank=True, null=True, help_text="Leave blank if currently studying")
    description = models.TextField(blank=True)
    grade = models.CharField(max_length=50, blank=True, help_text="e.g., First Class, 3.8 GPA")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ["-start_year", "order"]
        verbose_name = "Education"
        verbose_name_plural = "Education"
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"
    
    def year_range(self):
        if self.end_year:
            return f"{self.start_year} - {self.end_year}"
        return f"{self.start_year} - Present"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Languages', 'Programming Languages'),
        ('Frameworks', 'Frameworks & Libraries'),
        ('Tools', 'Tools & Platforms'),
        ('Databases', 'Databases'),
        ('Other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    proficiency = models.IntegerField(default=50, help_text="Proficiency level (0-100)")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.category})"