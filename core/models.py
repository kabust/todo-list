from django.utils import timezone
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(blank=True, default=False)
    tags = models.ManyToManyField(to=Tag, related_name="tasks")

    def is_past_deadline(self):
        if self.deadline:
            now = timezone.now()
            return self.deadline < now

    class Meta:
        ordering = ("is_done", "-created_at",)

    def __str__(self):
        return self.content
