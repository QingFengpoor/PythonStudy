from django.db import models

# Create your models here.

class Test(models.Model):  # table name in server is Test
    name = models.CharField(max_length=20)
    # name is the files in table. data type is CharField(like varchar),  
    # max_length is the limitation of length.
