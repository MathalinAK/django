#from django.db import models

#class home(models.Model):
 #   username=models.CharField (max_length=50)
  #  password=models.CharField (max_length=50)   

   # def __str__(self):
    #    return f"{self.username} - {self.password}"

    #Create your models here.
#from django.db import models

#class Homes(models.Model):
 #   username = models.CharField(max_length=50)
  #  password = models.CharField(max_length=50)  
   # contactnumber = models.IntegerField(null=True)
    #email = models.EmailField(null=True)

    #def __str__(self):
     #   return f"{self.username} - {self.password} -{ self.contactnumber} - {self.email}"
#dproj1/model.
#from django.db import models
#from django.contrib.auth.models import User
#from django.utils import timezone




#class Persondetails(models.Model):
 #   username = models.CharField(max_length=100, unique=True)  
  #  password = models.CharField(max_length=100)  
    #contactnumber = models.CharField(max_length=15, unique=True)  
   # email = models.EmailField(max_length=30,unique=True)#(widgets =models.TextInput(attrs={'readonly':'readonly'}))
    #images=models.ImageField(null = "True",blank = "True")

    #def __str__(self):
     #   return f"{self.username} - {self.password} - {self.email}"
    


#class UserProfile(models.Model):
 #   user = models.OneToOneField(User, on_delete=models.CASCADE)
  #  profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
   # address = models.TextField(null=True, blank=True)
    #city = models.CharField(max_length=100, null=True, blank=True)
  #  state = models.CharField(max_length=100, null=True, blank=True)
  #  postal_code = models.CharField(max_length=20, null=True, blank=True)

   # def __str__(self):
    #    return f"{self.user} - {self.address} - {self.city} - {self.state} - {self.postal_code} -{self.profile_image}"
    
    
#class OTPModel(models.Model):
  #  user = models.OneToOneField(User, on_delete=models.CASCADE)
   # otp = models.CharField(max_length=6)
    #created_at = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
     #   return f"OTP for {self.user.email}: {self.otp}"


#class OTP(models.Model):
 #   email = models.EmailField()  # Store the email associated with OTP
  #  otp = models.CharField(max_length=6)  # Store the 6-digit OTP
   # created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for OTP creation

    #def is_valid(self):
        # Check if the OTP is still valid (you can change the time limit)
     #   return (timezone.now() - self.created_at).seconds < 300
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class PersondetailsManager(BaseUserManager):
    def create_user(self, email, password=None, username=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        if username is None:
            username = ""  

        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password=None, username=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if username is None:
            username = "" 
        user = self.create_user(email, password, username=username, **extra_fields)
        return user
class Persondetails(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)

    objects = PersondetailsManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email if self.email else "No Email Provided"

        






    



