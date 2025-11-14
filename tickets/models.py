from django.db import models

# Create your models here.


class Ticket(models.Model):
    STATUS_CHOICES = [
        ("open", "Open"),
        ("in_progress", "In Progress"),
        ("closed", "Closed"),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="open")
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="tickets")

    def __str__(self):
        return f"{self.id}_{self.title}"
