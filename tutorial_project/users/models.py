from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    image = models.ImageField(default="default.png", upload_to="profile_pics")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username} Profile"
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            sizes = (300, 300)
            img.thumbnail(sizes)
            img.save(self.image.path)
