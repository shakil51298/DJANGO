from django.db import models

# Create your models here.

# adding MembersTable in our Database;

class MembersTable(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)