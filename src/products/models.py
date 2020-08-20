from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=30)
    alp_num_code = models.CharField(max_length=30)
    stock = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return "name: " + self.name.__str__() + \
               " alp_num_code: " + self.alp_num_code.__str__() + \
               " stock: " + self.stock.__str__() + \
               " description: " + self.description.__str__()
