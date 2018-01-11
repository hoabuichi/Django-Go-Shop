from __future__ import unicode_literals
import datetime

from django.db import models

# Create your models here.
# CREATE TABLE myapp_person (
#     "id" serial NOT NULL PRIMARY KEY,
#     "first_name" varchar(30) NOT NULL,
#     "last_name" varchar(30) NOT NULL,
#     "image_url" varchar(20000) NOT NULL
# );


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image_url = models.CharField(max_length=20000)
    date_of_birth = models.DateTimeField('date of birth', default=datetime.date.today)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + self.last_name