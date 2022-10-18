from django.db import models
from users.models import User

# Create your models here.
class Post(models.Model):
    class Meta:
        db_table = 'post'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to='images/',blank=True, null=True, default='')