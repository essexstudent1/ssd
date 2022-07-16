from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager #GROUP1 addition
from django.utils import timezone #GROUP1 addition

# Define a custom public user manager class
# This code is partially adapted from https://www.youtube.com/watch?v=eCeRC7E8Z7Y

class PublicUserManager(BaseUserManager):
    
    def create_user(self, email, password, security_question, security_answer, firstName, lastName, address, town, province, country, postcode):
        if not email:
            raise ValueError(_('The Email must be set'))
        if not security_question:
            raise ValueError(_('Security question must be set'))
        if not security_answer:
            raise ValueError(_('Security answer must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, security_question=security_question, security_answer=security_answer, firstName=firstName, lastName=lastName, address=address, town=town, province=province, country=country, postcode=postcode)
        user.set_password(password)
        #user.is_mfa_authenticated = False
        #user.mfa_attempts = 0
        user.save(using=self._db)
        return user
    
    #def create_superuser(self, email, password, security_question, security_answer, firstName, lastName, address, town, province, country, postcode):
       # email = self.normalize_email(email)
        #user = self.create_user(email=email, password=password, security_question=security_question, security_answer=security_answer, firstName=firstName, lastName=lastName, address=address, town=town, province=province, country=country, postcode=postcode)
       # user.set_password(password)
        #user.is_staff = True
       # user.is_superuser = True
       # user.save(using=self._db)
       # return user


# Define a new custom user class called PublicUser 

class PublicUser(AbstractBaseUser):
  firstName = models.CharField(verbose_name='First Name', help_text = 'Enter your first name.', max_length=100)
  lastName = models.CharField(verbose_name='Last Name', help_text = 'Enter your last name.', max_length=100)
  email = models.EmailField(verbose_name='Email Address', help_text = 'Enter your email address.',max_length=100, unique=True)
  address = models.CharField(verbose_name='Street Address', help_text = 'Enter your street name and number, including unit number if applicable.',max_length=100)
  town = models.CharField(verbose_name='City or town', help_text = 'Enter your city, town, or village.',max_length=100)
  province = models.CharField(verbose_name='State or Province', help_text = 'Enter your state or province.',max_length=100)
  country = models.CharField(verbose_name='Country', help_text = 'Enter your country.',max_length=100)
  postcode = models.CharField(verbose_name='Postal Code', help_text = 'Enter your postal code.',max_length=100)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_superuser = models.BooleanField(default=False)
  date_joined = models.DateTimeField(default=timezone.now)
  security_question = models.CharField(verbose_name='Security Question', help_text = 'Enter a security question that only you will know the answer to.', max_length=255)
  security_answer = models.CharField(verbose_name='Security Answer', help_text = 'Enter the answer to the above security question.',max_length=50)
  is_mfa_authenticated = models.BooleanField(default=False)
  mfa_attempts = models.IntegerField(default=0)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['security_question', 'security_answer']

  objects = PublicUserManager()

  def __str__(self):
        return self.email




class Report(models.Model):
    person_id = models.CharField(max_length=10)
    data_breach_details = models.TextField(max_length=1000)
    responsible_party = models.TextField(max_length=1000)
    others_notified = models.IntegerField()
    data_breach_noticed_on = models.DateField()

    def __str__(self):
        return self.person_id


