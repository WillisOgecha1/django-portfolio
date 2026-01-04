from django.db import models


class Experience(models.Model):
    year = models.CharField(max_length=10)
    role = models.CharField(max_length=100)
    organization = models.CharField(max_length=150)
    description = models.TextField()
    skills = models.TextField(
        help_text="Comma-separated skills",
        default=""
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-year", "order"]

    def skill_list(self):
        return [skill.strip() for skill in self.skills.split(",") if skill.strip()]

    def __str__(self):
        return f"{self.role} - {self.organization}"


class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=150)
    issue_date = models.DateField()
    credential_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["-issue_date"]

    def __str__(self):
        return self.name