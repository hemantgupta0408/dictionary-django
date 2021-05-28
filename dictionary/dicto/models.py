from dictionary.settings import UPLOAD_URL
from django.db import models

# Create your models here.
class Words(models.Model):
    eword = models.CharField(max_length=30 ,  unique=True)
    hword = models.CharField(max_length=30)
    uses = models.CharField(max_length=120)
    category = models.CharField(max_length=80)
    image = models.ImageField(upload_to="upload/")
    rword = models.CharField(max_length=30)
    
    def __str__(self):
        return self.eword    
    
    class Meta:
        db_table = "Words"


    
    