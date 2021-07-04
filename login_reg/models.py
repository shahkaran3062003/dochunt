from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.


class collage(models.Model):
    u_id = models.AutoField(primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    user_name = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column="username")
    coll_type = models.CharField(max_length=7, default="")

    def __str__(self):
        return str(self.user_name)
