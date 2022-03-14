from django.db import models

class Register(models.Model):
    CHOICES = (
        ('Beginner', 'Beginner'),
        ('Elementary', 'Elementary'),
        ('Pre Intermediate', 'Pre Intermediate'),
        ('Intermediate', 'Intermediate'),
        ('Upper Intermediate', 'Upper Intermediate'),
        ('Advanced', 'Advanced'),
        ('IELTS', 'IELTS'),
    )
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    degree = models.CharField(max_length=200, choices=CHOICES)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ('-id',)


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ('-id',)
