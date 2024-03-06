import uuid
from django.db import models
from core.models import User, Skill, Proficiency

class UserSkill(models.Model):
    class Meta:
        app_label = 'core'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency = models.ForeignKey(Proficiency, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - {self.skill.skill_name} - {self.proficiency.level}"

class UserSkillsHistory(models.Model):
    class Meta:
        app_label = 'core'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skill_history')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency = models.ForeignKey(Proficiency, on_delete=models.CASCADE)
    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History: {self.user.email} - {self.skill.skill_name} - {self.proficiency.level} at {self.changed_at}"