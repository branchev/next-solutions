# IMPLEMENTED IN THIS TABLE BECAUSE OF THE CONDITIONS FOR THE BUSINESS LOGIC OF THE TASK
# AND TO BEE EASY TO EXTEND IF VIN AND OTHER SERIAL NUMBERS NEEDED.


from django.db import models


class BGRegNumber(models.Model):
    bg_reg_number = models.CharField(
        max_length=8,
        unique=True,
        blank=False,
    )

    def __str__(self):
        return self.bg_reg_number
