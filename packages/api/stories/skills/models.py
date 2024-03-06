import uuid
from django.db import models

class Skill(models.Model):
    class Meta:
        app_label = 'core'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    skill_name = models.CharField(max_length=255)
    is_predefined = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.skill_name

class SkillTag(models.Model):
    class Meta:
        app_label = 'core'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='tags')
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name

class Proficiency(models.Model):
    class Meta:
        app_label = 'core'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    level = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.level
