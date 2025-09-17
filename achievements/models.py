from django.db import models

# Achievement Model with name
class Achievement(models.Model):
    name = models.CharField(max_length=255) # Name of the achievement

    class Meta:
        db_table = 'Achievement'

    def __str__(self):
        return self.name

