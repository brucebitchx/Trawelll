from django.db import models

class Places(models.Model):
    place_name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    raiting = models.CharField(max_length=55)

    def __str__(self):
        return self.place_name


class Packages(models.Model):
    package_name = models.CharField(max_length=255)
    desc = models.CharField(max_length=1024)
    contact = models.EmailField()
    pic = models.ImageField(upload_to='media/')
    places = models.ManyToManyField(to=Places)

    def __str__(self):
        return self.package_name
    

class Travel(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    contact = models.CharField(max_length=55)
    image = models.ImageField(upload_to='uploads/travels_image')
