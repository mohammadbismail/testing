from django.db import models
import re


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters!"
        if not (postData['first_name']).isalpha():
            errors['first_name'] = "Please use only letters, check your First Name!"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters!"
        if not (postData['last_name']).isalpha():
            errors['last_name'] = "Please use only letters, check your Last Name!"
        if len(postData['password']) < 8:
            errors['password'] = "Passoword should be at least 8 characters!"
        if (postData["password"]) != postData["confirm_password"]:
            errors["confirm_password"] = "your passwords did not match"

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # liked_books = a list of books a given user likes
    #books_uploaded = a list of books uploaded by a given user
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
