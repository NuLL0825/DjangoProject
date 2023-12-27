from django.core.management.base import BaseCommand
from myapp.models import Employee, JobPosition, ContractType, Institution, ServiceRecord

class Command(BaseCommand):
    help = 'Creates initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_employee_data()

    def create_employee_data(self):
        employee1 = Employee(first_name = "Maui Azryl", last_name = "Lomuntad", sex = "Male", birthdate = "2002-08-25", location = "Puerto Princesa", email = "maui@gmail.com")
        employee2 = Employee(first_name = "Joshua Serge", last_name = "Tibudan", sex = "Male", birthdate = "1991-02-02", location = "Kyoto", email = "js@gmail.com")
        employee3 = Employee(first_name = "Albert", last_name = "Mirasol", sex = "Male", birthdate = "2002-08-26", location = "Kuala Lumpur", email = "jobert@gmail.com")
        employee4 = Employee(first_name = "Zaj Kenneth", last_name = "Panes", sex = "Male", birthdate = "2002-09-6", location = "Puerto Princesa", email = "ooshushi@gmail.com")
        employee5 = Employee(first_name = "Rovick Anthony", last_name = "Pasamonte", sex = "Male", birthdate = "2003-05-26", location = "Puerto Princesa", email = "robik@gmail.com")

        employee1.save()
        employee2.save()
        employee3.save()
        employee4.save()
        employee5.save()

        self.stdout.write(self.style.SUCCESS(
            "Successfully Created Employees."
        ))