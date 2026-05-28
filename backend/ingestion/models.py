from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class EmissionRecord(models.Model):

    REVIEW_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('FLAGGED', 'Flagged'),
    ]

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    source_type = models.CharField(max_length=50)

    activity_type = models.CharField(max_length=100)

    quantity = models.FloatField()

    unit = models.CharField(max_length=50)

    scope = models.CharField(max_length=20)

    review_status = models.CharField(
        max_length=20,
        choices=REVIEW_STATUS_CHOICES,
        default='PENDING'
    )

    locked = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} - {self.quantity} {self.unit}"