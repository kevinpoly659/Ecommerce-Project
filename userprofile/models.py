from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
import uuid

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self,username, email,first_name,last_name, password ,phone_number):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email          = self.normalize_email(email),
            username       = username,
            first_name  = first_name,
            last_name   = last_name,
            phone_number = phone_number,
            is_admin= False,
            is_active=True,
            is_staff=False,
            is_superuser=False,
        ) 
   
        user.set_password(password)
        user.save(using=self._db)
        return user
 

    def create_superuser(self, first_name,last_name,email,username, password,phone_number):
        user = self.create_user(
            email       = self.normalize_email(email),
            username    = username,
            password    = password,
            first_name  = first_name,
            last_name   = last_name,
            phone_number =phone_number,
        )
        user.is_admin= True
        user.is_active=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

 
class Account(AbstractBaseUser):
       first_name    = models.CharField(max_length=50,null=True)
       last_name     = models.CharField(max_length=50,null=True )
       username      = models.CharField(max_length=50,unique=True)
       email         = models.EmailField(max_length=100, unique=True)
       phone_number  = models.CharField(max_length=50, unique=True,null=True)
       otp           = models.CharField(max_length=100, null=True, blank=True)



       #required
       date_joined     = models.DateTimeField(auto_now_add=True)
       last_login      = models.DateTimeField(auto_now_add=True)
       is_admin        = models.BooleanField(default=False)
       is_staff        = models.BooleanField(default=False)
       is_active       = models.BooleanField(default=True)
       is_superuser    = models.BooleanField(default=False)
       

       USERNAME_FIELD ='username'
       REQUIRED_FIELDS=['first_name','last_name','phone_number']

       objects=MyAccountManager()

       def _str_(self):
             return self.email

       def has_perm(self,perm, obj=None):  
           return self.is_admin  
    
       def has_module_perms(self, add_label):
        return True    


class Address(models.Model):
    firstname           =   models.CharField(max_length=50 ,null=True)
    lastname            =   models.CharField(max_length=50 ,null=True)
    phone_number        =   models.CharField(max_length=50 ,null=True)
    Email_Address       =   models.EmailField(max_length=50 ,null=True)
    Addressfield        =   models.CharField(max_length=50 ,null=True) 
    Town                =   models.CharField(max_length=50 ,null=True) 
    state               =   models.CharField(max_length=50 ,null=True) 
    pincode             =   models.CharField(max_length=50 ,null=True)
    user                =   models.ForeignKey(Account,on_delete=models.CASCADE, null=True) 

    def __unicode__(self):
        return self.firstname       
    

class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name= 'profile')
    uid = models.UUIDField(default=uuid.uuid4)
    phone_number = models.CharField(max_length=15)
    
class Guest(models.Model):
    name = models.CharField(max_length=200,default='guest')
    uid = models.UUIDField(default=uuid.uuid4)