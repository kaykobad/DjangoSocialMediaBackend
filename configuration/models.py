from django.db import models


class Country(models.Model):
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class Language(models.Model):
    language = models.CharField(max_length=255)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class Religion(models.Model):
    religion = models.CharField(max_length=255)

    def __str__(self):
        return self.religion

    class Meta:
        verbose_name = 'Religion'
        verbose_name_plural = 'Religions'


