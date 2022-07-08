from django.db import models

# Define a new custom user class called User as per design document

class User(AbstractBaseUser):
  firstName = models.CharField(verbose_name='First Name', help_text = 'Enter your first name.', max_length=100)
  lastName = models.CharField(verbose_name='Last Name', help_text = 'Enter your last name.', max_length=100)
  email = models.EmailField(verbose_name='Email Address', help_text = 'Enter your email address.',max_length=100, unique=True)
  username = models.CharField(verbose_name='Username', help_text = 'Enter a username.',max_length=100, unique=True)
  address = models.CharField(verbose_name='Street Address', help_text = 'Enter your street name and number, including unit number if applicable.',max_length=100)
  town = models.CharField(verbose_name='City or town', help_text = 'Enter your city, town, or village.',max_length=100)
  province = models.CharField(verbose_name='State or Province', help_text = 'Enter your state or province.',max_length=100)
  country = models.CharField(verbose_name='Country', help_text = 'Enter your country.',max_length=100)
  postcode = models.CharField(verbose_name='Postal Code', help_text = 'Enter your postal code.',max_length=100)
  is_superuser = models.BooleanField(default=False)
  registeredOn = models.DateTimeField(default=timezone.now)

  #These lines are from Kate's 2FA POC assignment. Remove them if not needed before submitting.  
  #security_question = models.CharField(verbose_name='Security Question', help_text = 'Enter a security question that only you will know the answer to.', max_length=255)
  #security_answer = models.CharField(verbose_name='Security Answer', help_text = 'Enter the answer to the above security question.',max_length=50)
  #is_mfa_authenticated = models.BooleanField(default=False)
  #mfa_attempts = models.IntegerField(default=0)
  
  
  
  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['username', 'email']

  objects = PatientUserManager()

  def __str__(self):
        return self.email
