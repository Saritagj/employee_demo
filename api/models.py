from django.db import models

# Department and Comapany are master table (Changes are not made frequently)
# Employee is transition table (Changes made frequently)

GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
)

class MCompany(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    delete_status = models.BooleanField(blank=True, null=True)
    created_user_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_user_id = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
   
   
class MDepartment(models.Model):
    name = models.CharField(max_length=100)    
    delete_status = models.BooleanField(blank=True, null=True)
    created_user_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_user_id = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class TEmployee(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    department = models.ForeignKey(
        MDepartment, on_delete=models.CASCADE, null=True
    )
    company = models.ForeignKey(MCompany, on_delete=models.CASCADE, null=True)
    delete_status = models.BooleanField(blank=True, null=True)
    created_user_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_user_id = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
