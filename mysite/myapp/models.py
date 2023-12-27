from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Employee(BaseModel):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    sex = models.CharField(max_length=7, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.first_name
    
class JobPosition(BaseModel):
    category = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self) :
        return self.category

class ContractType(BaseModel):
    classification = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) :
        return self.classification

class Institution(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) :
        return self.name

class ServiceRecord(BaseModel):
    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE)
    job_position = models.ForeignKey(JobPosition, blank=True, null=True, on_delete=models.CASCADE)
    contract_type = models.ForeignKey(ContractType, blank=True, null=True, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, blank=True, null=True, on_delete=models.CASCADE)
    monthly_salary = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self) :
        return f"{self.employee.first_name} {self.employee.last_name}"