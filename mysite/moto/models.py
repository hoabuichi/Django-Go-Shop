from django.db import models

# Create your models here.
# many-to-one relationship


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)


class Car(models.Model):
    # foreignKey field name should be the name of the Model in lowercase
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

# many to many relationship


class Topping(models.Model):
    pass


class Pizza(models.Model):
    # the name of ManyToManyField should be the plural version of the Model
    # it does not matter which model will have ManyToManyField, but it should be existed in only one model, not both
    toppings = models.ManyToManyField(Topping)

# extra fields in many to many relationship


class Person(models.Model):
    name = models.CharField(max_length=128)


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


# meta data
class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"
        # ordering, database - table name

