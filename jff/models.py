from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Office(models.Model):
    company = models.ForeignKey(Company, models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
