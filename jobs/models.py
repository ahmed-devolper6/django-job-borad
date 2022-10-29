from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
JOB_TYPE = [
    ('Remote' , 'Remote'),
    ('Hyperd' , 'Hyperd'),
    ('On-site' , 'On-site'),
]
# Create your models here.
class Jobs(models.Model):
    user = models.OneToOneField(User, on_delete = models.SET_NULL, null = True)
    title = models.CharField(max_length = 20)
    job_type = models.CharField(max_length = 19 , choices =JOB_TYPE)
    catgory = models.CharField(max_length = 15)
    requiremnt = models.TextField(max_length = 50)
    salary = models.CharField(max_length = 35)
    country = models.CharField(max_length = 15)
    description = models.TextField(max_length = 50)
    Benefits = models.TextField(max_length = 50)
    publish_date = models.DateTimeField(default = timezone.now)
    def __str__(self) -> str:
        return self.title

class Apply(models.Model):
    job = models.ForeignKey(Jobs, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)
    cover_letter = models.TextField(max_length = 50)
    email = models.EmailField()
    job = models.ForeignKey(Jobs,on_delete = models.SET_NULL, null = True)
    def __str__(self) -> str:
        return f"{self.name} - {str(self.job)}"
