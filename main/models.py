from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class NinjaManager(models.Manager):
    def basic_validator(self, post_data):

        errors = {}

        if len(post_data["first_name"]) < 1:
            errors["first_name"] = "Please enter your first name!"
        if len(post_data["last_name"]) < 1:
            errors["last_name"] = "Please enter your last name!"
        if len(post_data["dojo_id"]) < 1:
            errors["dojo"] = "Please select your dojo!"

        return errors

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE, related_name="ninjas")

    objects = NinjaManager()