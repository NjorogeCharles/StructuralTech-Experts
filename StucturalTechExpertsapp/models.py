from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


class Quote(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.CharField(max_length=200)
    comment = models.TextField()

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name