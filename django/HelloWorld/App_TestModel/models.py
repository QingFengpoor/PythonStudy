from django.db import models

# Create your models here.

class Test(models.Model):  # table name in server is Test
    name = models.CharField(max_length=20)
    # name is the files in table. data type is CharField(like varchar),  
    # max_length is the limitation of length.

class Contact(models.Model):    
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
