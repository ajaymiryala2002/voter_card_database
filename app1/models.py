import uuid
from django.db import models

def generate_voter_id():
    return "VTR" + uuid.uuid4().hex[:8].upper()

class Voter(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )

    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)

    voter_id_no = models.CharField(max_length=20, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.voter_id_no:
            self.voter_id_no = generate_voter_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name
