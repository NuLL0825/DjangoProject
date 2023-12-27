from django.contrib import admin

# Register your models here.
from .models import Employee, JobPosition, ContractType, Institution, ServiceRecord

# admin.site.register(Employee)
# admin.site.register(JobPosition)
# admin.site.register(ContractType)
# admin.site.register(Institution)
# admin.site.register(ServiceRecord)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "sex", "birthdate", "location", "email", "created_at", "updated_at")
    search_fields = ("first_name",)

@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ("category", "description", "created_at", "updated_at")
    search_fields = ("category",)

@admin.register(ContractType)
class ContractTypeAdmin(admin.ModelAdmin):
    list_display = ("classification", "description", "created_at", "updated_at")
    search_fields = ("classification",)

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)

@admin.register(ServiceRecord)
class ServiceRecordAdmin(admin.ModelAdmin):
    list_display = ("employee", "job_position", "contract_type", "institution", "monthly_salary", "start_date", "end_date", "created_at", "updated_at")
    search_fields = ("employee",)
