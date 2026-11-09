"""
URL configuration for fleet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from fleetmanagement.views import home_view, car_form, edit_car, staff_form, edit_staff, assign_form, edit_assignment, fuelling_form, edit_fuel, repair_issues_form, service_issues_form, repair_records_form, service_records_form, edit_repair_issues, edit_service_issues, edit_repair_records, edit_service_records, delete_car_form, delete_staff_form, delete_assign_form, delete_fuel_form, delete_repair_issues_form, delete_service_issues_form, delete_repair_records_form, delete_service_records_form, sign_up_view
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_up/', sign_up_view, name='sign_up_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home_view, name='home_page'),
    path('car/', car_form, name='car_page'),
    path('edit_car/<int:car_id>/', edit_car, name='edit_car_page'),
    path('delete_car/<int:car_id>/', delete_car_form, name='delete_car_page'),
    path('staff/', staff_form, name='staff_page'),
    path('edit_staff/<int:staff_id>/', edit_staff, name='edit_staff_page'),
    path('delete_staff/<int:staff_id>/', delete_staff_form, name='delete_staff_page'),
    path('assignment/', assign_form, name='assignment_page'),
    path('edit_assignment/<int:assignmentid>/', edit_assignment, name='edit_assignment_page'),
    path('delete_assignment/<int:assignmentid>/', delete_assign_form, name='delete_assignment_page'),
    path('fuelling/', fuelling_form, name='fuelling_page'),
    path('edit_fuel/<int:fuelid>/', edit_fuel, name='edit_fuel_page'),
    path('delete_fuel/<int:fuel_id>/', delete_fuel_form, name='delete_fuel_page'),
    path('repairissues/', repair_issues_form, name='repair_issues_page'),
    path('editrepairissues/<int:repairissuesid>/', edit_repair_issues, name='edit_repair_issues_page'),
    path('delete_repair_issues/<int:repair_issues_id>/', delete_repair_issues_form, name='delete_repair_issues_page'),
    path('serviceissues/', service_issues_form, name='service_issues_page'),
    path('editserviceissues/<int:serviceissuesid>/', edit_service_issues, name='edit_service_issues_page'),
    path('delete_service_issues/<int:service_issues_id>/', delete_service_issues_form, name='delete_service_issues_page'),
    path('servicerecords/', service_records_form, name='service_records_page'),
    path('servicerecords/<int:servicerecordsid>/', edit_service_records, name='edit_service_records_page'),
    path('delete_repair_records/<int:repair_records_id>/', delete_repair_records_form, name='delete_repair_records_page'),
    path('repairrecords/', repair_records_form, name='repair_records_page'),
    path('repairrecords/<int:repairrecordsid>/', edit_repair_records, name='edit_repair_records'),
    path('delete_service_records/<int:service_records_id>/', delete_service_records_form, name='delete_service_records_page')
]
