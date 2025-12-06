import uuid
from django.db import models

def generate_voter_id():
    return "VTR" + uuid.uuid4().hex[:8].upper()

class Voter(models.Model):
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=200)
    voter_id_no = models.CharField(max_length=20, unique=True, blank=True)
    photos = models.ImageField(upload_to="photos/", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.voter_id_no:
            self.voter_id_no = generate_voter_id()
        super().save(*args, **kwargs)
