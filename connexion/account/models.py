from django.db import models

# Create your models here.
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', 
                              blank=True)
    status = models.CharField(blank=True,max_length=250)
    RegistrationID = models.CharField(blank=True, max_length = 12)
    
    Profile_types = (('ST','Student'),('FC','Faculty'),('AL','Alumni'))
    Profile_type = models.CharField(default='ST', max_length=2,choices=Profile_types)
    
    SexTypes = (('M','Male'),('F','Female'),('D','default'))
    Sex_Type = models.CharField(default='D',max_length=1,choices=SexTypes)
    
    Career = models.CharField(blank=True,max_length=60)

    Clubs = (('R','Rotaract'),('I','IEEE'),('A','ACM'),('E','IE'),('N','None'))
    Exclusive_Club = models.CharField(max_length=1,default='N',choices=Clubs)

    Other_Clubs = models.CharField(blank=True,max_length=60)

    Description  = models.TextField(blank=True)


    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)