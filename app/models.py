from django.db import models
from .validators import validate_file_extension

# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/',validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)