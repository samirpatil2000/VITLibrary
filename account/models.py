from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from books.choices import STREAM,YEAR

class MyAccountManager(BaseUserManager):
	def create_user(self, email, password=None):

		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=self.normalize_email(email),
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):

		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
		)
		user.is_admin     = True
		user.is_staff     = True
		user.is_superuser = True

		user.save(using=self._db)
		return user


def validate_geeks_mail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("This field accepts mail id of google only")


class Account(AbstractBaseUser):

	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True,blank=True,null=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)


	# All these field are required for custom user model
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)

	# other
	first_name             = models.CharField(max_length=20,blank=True,null=True)
	last_name              = models.CharField(max_length=20,blank=True,null=True)

	branch                 = models.CharField(choices=STREAM,max_length=30,blank=True,null=True)
	year                   = models.CharField(choices=YEAR,max_length=30,blank=True,null=True)



	is_classcr            = models.BooleanField(default=False)


	# phone_number = PhoneNumberField(default='1234567890')

	USERNAME_FIELD = 'email'   # This with login with email
	REQUIRED_FIELDS = []  # other than email

	objects= MyAccountManager()

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True
