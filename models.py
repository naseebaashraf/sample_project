from django.db import models

# Create your models here.
class user_login(models.Model):
    #id
    uname = models.CharField(max_length=50)
    passwd = models.CharField(max_length=25)
    utype = models.CharField(max_length=10)

    def __str__(self):
        return self.uname

class pic_pool(models.Model):
    pic_path = models.CharField(max_length=250)
    dt = models.CharField(max_length=30)
    tm = models.CharField(max_length=30)

class student(models.Model):
    #id
    sregno= models.CharField(max_length=50)
    sname = models.CharField(max_length=25)
    scourse = models.CharField(max_length=10)


    def __str__(self):
        return self.sname


