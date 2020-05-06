from django.db import models
from djongo import models
#from djongo import forms

# Create your models here.
class UserRequests(models.Model):
    #id = models.IntegerField(primary_key=True)
    OHRID= models.IntegerField()
    url=models.URLField(max_length=250)
    subnet=models.CharField(max_length=200)
    date=models.DateField()
    starttime=models.TimeField()
    endtime=models.TimeField()
    frequency=models.IntegerField()
    completed=models.BooleanField(default=False)
    #objects = models.Manager()
    class Meta:
        db_table="ui_table_data"
    def __str__(self):
        return str(self.OHRID) + ' ' + str(self.completed)