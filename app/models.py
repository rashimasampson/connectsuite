from django.db import models
import re
import bcrypt
# Create your models here.

class BrandManager(models.Manager):
    def brand_validator(self, postData):
        errors = {}
        # checks the email 
        email_regex = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['password']) > 8:
            errors['password'] = "Your password must be at least 8 characters"
        if len(postData['company_name']):
            errors['company_name'] = "Your name must be at least 3 characters"
        if not email_regex.match(postData['email']):
            errors['email'] = 'Email must be valid'
        email_check = self.filter(email=postData['email'])
        if email_check:
            errors['email'] = "Email already in use"
        if postData['password'] != postData['confirm']:
            errors['password'] = 'Password and Confirm PW do not match'
        return errors
    def brand_authenticate(self, postData):
        errors = {}
        check = Brand.objects.filter(email=postData['email'])
        if not check:
            errors['email'] = "Email has not been registered."
        else:
            if not bcrypt.checkpw(postData['password'].encode(), check[0].password.encode()):
                errors['email'] = "Email and password do not match."
        return errors

class Brand(models.Model):
    company_name = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    company_city = models.CharField(max_length=25)
    company_state = models.CharField(max_length=25)
    job_description = models.TextField(null=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    objects = BrandManager()

class TalentManager(models.Manager):
    def talent_validator(self, postData):
        errors = {}
        # checks the email 
        email_regex = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['password']) > 8:
            errors['password'] = "Your password must be at least 8 characters"
        if len(postData['first_name']) < 2 or len(postData['last_name']) < 2:
            errors['first_name'] = "Your name must be at least 3 characters"
        if not email_regex.match(postData['email']):
            errors['email'] = 'Email must be valid'
        email_check = self.filter(email=postData['email'])
        if email_check:
            errors['email'] = "Email already in use"
        if postData['password'] != postData['confirm']:
            errors['password'] = 'Password and Confirm PW do not match'
        return errors
    def talent_authenticate(self, postData):
        errors = {}
        check = Talent.objects.filter(email=postData['email'])
        if not check:
            errors['email'] = "Email has not been registered."
        else:
            if not bcrypt.checkpw(postData['password'].encode(), check[0].password.encode()):
                errors['email'] = "Email and password do not match."
        return errors

class Talent(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    instagram_handle = models.CharField(max_length=25)
    niche = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    influencer = models.ManyToManyField(Brand, related_name='promoter', null=True)
    likes = models.ManyToManyField(Brand, related_name='favorite_talent')
    objects = TalentManager()
