from PIL import Image
from django.db import models
from django.contrib.auth.models import User

from main.models import Armwrestler


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image = models.ImageField(default="default.jpg", upload_to='profile_pics')
    armwrestler = models.ForeignKey(Armwrestler, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.armwrestler.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
        img.save(self.armwrestler.image.path)
