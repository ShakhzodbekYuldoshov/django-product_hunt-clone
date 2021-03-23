from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    url = models.TextField()
    pub_date = models.DateTimeField()
    votes_total = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to="images/")
    icon = models.ImageField(upload_to="images/")
    hunter = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title
    

    def summary(self):
        return self.body[:100]


    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
