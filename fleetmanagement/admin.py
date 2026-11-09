from django.contrib import admin
from .models import Car, Staff, Assigning, Fuelling, Repair_issues, Repair_records, Service_issues, Service_records

class Caradmin(admin.ModelAdmin):
    list_display = ("car_type", "number_plate", "Brand", "Model", "Expiry_insurance", "Transmission", "Engine_type")

class Staffadmin(admin.ModelAdmin):
    list_display = ("first_name", "second_name", "gender", "role")

class Assigningadmin(admin.ModelAdmin):
    list_display = ("staff_id", "number_plate", "assignment_date")

class Fuellingadmin(admin.ModelAdmin):
    list_display = ("vehicle_id", "station", "quantity", "price", "total_cost", "date")

class Repair_issues_admin(admin.ModelAdmin):
    list_display = ("problem", "quantity", "measure", "unit_cost")

class Repair_records_admin(admin.ModelAdmin):
    list_display = ("repair_id", "Vehicle_id", "repair_center", "cost", "repair_date")

class Service_issues_admin(admin.ModelAdmin):
    list_display = ("service_item", "quantity", "measure", "unit_cost")

class Service_records_admin(admin.ModelAdmin):
    list_display = ("Service_id", "Vehicle_id", "service_center", "cost", "sercice_date")

admin.site.register(Car, Caradmin)
admin.site.register(Staff, Staffadmin)
admin.site.register(Assigning, Assigningadmin)
admin.site.register(Fuelling, Fuellingadmin)
admin.site.register(Repair_issues, Repair_issues_admin)
admin.site.register(Repair_records, Repair_records_admin)
admin.site.register(Service_issues, Service_issues_admin)
admin.site.register(Service_records, Service_records_admin)




