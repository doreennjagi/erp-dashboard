from django.db import models
from django.contrib.auth.models import User

class UploadedFile(models.Model):
    FILE_TYPE_CHOICES = [
        ('csv', 'CSV'),
        ('excel', 'Excel'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return self.file_name
