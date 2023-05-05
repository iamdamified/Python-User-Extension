from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# INBUILT USER EXTENSION MODEL FOR COLLECTIMG NEW USERS
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # This line links a registering a user automaticlly to his DBASE profile from frontend
    profile_picture = models.ImageField(default='default2.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.user} profile"
    

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
