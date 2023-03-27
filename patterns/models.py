from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

SKILL_LEVEL_CHOICES = [
    ('Easy', 'Easy'),
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
]

REGION_CHOICES = [
    ('UK', 'UK'),
    ('US', 'US'),
]


class CrochetPattern(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    skill_level = models.CharField(max_length=100, choices=SKILL_LEVEL_CHOICES)
    region = models.CharField(max_length=100, choices=REGION_CHOICES)
    yarn_weight = models.CharField(max_length=100)
    hook_size = models.CharField(max_length=100)
    gauge = models.CharField(max_length=100)
    pattern = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title


class CrochetPatternForm(ModelForm):
    class Meta:
        model = CrochetPattern
        fields = ['title', 'description', 'skill_level', 'region', 'yarn_weight',
                  'hook_size', 'gauge', 'pattern', 'image']
