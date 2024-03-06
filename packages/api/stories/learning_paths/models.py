import uuid
from django.db import models
from core.models import User

class LearningPath(models.Model):
    class Meta:
        app_label = 'core'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='learning_paths')
    title = models.CharField(max_length=255)
    path_type = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PathModule(models.Model):
    class Meta:
        app_label = 'core'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    path = models.ForeignKey(LearningPath, on_delete=models.CASCADE, related_name='modules')
    skill = models.ForeignKey('core.Skill', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    estimated_completion_time = models.IntegerField()
    module_order = models.IntegerField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserInterestsAndGoals(models.Model):
    class Meta:
        app_label = 'core'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interests_goals')
    title = models.CharField(max_length=255)
    interest = models.TextField()
    goal = models.TextField()
    time_frame = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Feedback(models.Model):
    class Meta:
        app_label = 'core'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback')
    path = models.ForeignKey(LearningPath, on_delete=models.CASCADE, related_name='feedback')
    feedback_text = models.TextField()
    is_positive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ModuleFeedback(models.Model):
    class Meta:
        app_label = 'core'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='module_feedback')
    module = models.ForeignKey(PathModule, on_delete=models.CASCADE, related_name='feedback')
    feedback_text = models.TextField()
    is_positive = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
