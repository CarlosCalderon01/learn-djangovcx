from django.db import models

# Create your models here.
class Task(models.Model):
    # id = models.AutoField()
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Task'
    
    def __str__(self):
        return self.title

