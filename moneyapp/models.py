from django.db import models
from django.contrib.auth.models import User

class Statement(models.Model):
    name = models.CharField(max_length=100,null=True)
    amount = models.IntegerField(null=True)
    choices=(
        ("income","รายรับ"),
        ("expense","รายจ่าย")
    )
    category = models.CharField(max_length=100,choices=choices,default=1,null=True)
    date = models.DateTimeField(auto_now_add=True)
    manager = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    cover = models.ImageField(upload_to='images',blank=True)
