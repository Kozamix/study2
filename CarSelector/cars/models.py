from django.db import models

class Car(models.Model):

    year = models.IntegerField()
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='car_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"
