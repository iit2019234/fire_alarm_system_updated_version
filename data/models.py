from django.db import models

# Create your models here.
class sensor_info(models.Model):
    flame_val = models.FloatField(null=True)
    smoke_val = models.FloatField(null=True)
    temp_val = models.FloatField(null=True)
    date_created=models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
    
        return str(self.date_created)
