from django.db import models

class Child(models.Model):
    STATUS_CHOICES = [
        ('lead', 'Лид'),
        ('client', 'Клиент'),
    ]

    full_name = models.CharField(max_length=200)
    cyberons = models.IntegerField(default=0)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='lead',
    )

    def __str__(self):
        return f'{self.full_name} ({self.get_status_display()})'
