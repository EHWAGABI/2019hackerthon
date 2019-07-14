from django.db import models
#from django.contrib.auth import get_user_model
# Create your models here.

class Market(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)
    body = models.TextField(default='')

    def __str__(self):
        return self.title
    #author =  models.ForeignKey(
    #    get_user_model(),
    #    on_delete=models.CASCADE
    #)
    #file=models.FileField(null=True)
