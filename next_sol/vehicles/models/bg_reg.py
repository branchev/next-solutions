from django.db import models


class BGRegNumber(models.Model):
    bg_reg_number = models.CharField(
        max_length=10,
        unique=True,
        blank=False,
    )

