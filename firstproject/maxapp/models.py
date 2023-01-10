from django.db import models

# Create your models here.

class patients(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    dob=models.DateField()
    gender=models.CharField(max_length=20)

    def __str__(self):
        return self.fname

    #JSON

    # def get_data(self):
    #     return{
    #         'id':self.id,
    #         'fname':self.fname,
    #         'lname':self.lname,
    #         'dob':self.dob,
    #         'gender':self.gender,
    #     }

