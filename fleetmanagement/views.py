from datetime import date, timedelta
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from fleetmanagement.forms import CarForm, StaffForm, AssigningForm, FuellingForm, Repair_issuesForm, Service_issuesForm, Repair_recordsForm, Service_recordsForm
from fleetmanagement.models import Car, Staff, Assigning, Fuelling, Repair_issues, Service_issues, Repair_records, Service_records

@login_required
def home_view(request):
    # One card per section: title, how many records it has, and the page it links to
    cards = [
        {'title': 'Cars', 'emoji': '🚗', 'count': Car.objects.count(), 'link': 'car_page'},
        {'title': 'Staff', 'emoji': '👷', 'count': Staff.objects.count(), 'link': 'staff_page'},
        {'title': 'Assignments', 'emoji': '📋', 'count': Assigning.objects.count(), 'link': 'assignment_page'},
        {'title': 'Fuel records', 'emoji': '⛽', 'count': Fuelling.objects.count(), 'link': 'fuelling_page'},
        {'title': 'Repair issues', 'emoji': '🔧', 'count': Repair_issues.objects.count(), 'link': 'repair_issues_page'},
        {'title': 'Service issues', 'emoji': '🛠️', 'count': Service_issues.objects.count(), 'link': 'service_issues_page'},
    ]

    # Cars whose insurance has expired or will expire in the next 30 days
    in_30_days = date.today() + timedelta(days=30)
    expiring_cars = Car.objects.filter(Expiry_insurance__lte=in_30_days).order_by('Expiry_insurance')

    context = {
        'cards': cards,
        'expiring_cars': expiring_cars,
        'today': date.today(),
    }
    return render(request, 'dashboard.html', context)

@login_required
def car_form(request):
    message = ''
    if request.method == 'POST':
        carform = CarForm(request.POST)

        if carform.is_valid():
            carform.save()
            message = 'A car has been added successfully'
            return redirect('car_page')
    else:
        carform = CarForm()

    car = Car.objects.all()

    context = {
        'form' : carform,
        'msg' : message,
        'car' : car
    }
    return render(request, 'car.html', context)

@login_required
def edit_car(request, car_id):
    car = Car.objects.get(id = car_id)
    message = ''

    if request.method == "POST":
        car_form = CarForm(request.POST, instance=car)

        if car_form.is_valid():
            car_form.save()
            return redirect('car_page')
        else:
            message = "Form has invalid data"

    else:
        car_form = CarForm(instance=car)

    context = {
        'form' : car_form,
        'car' : car,
        'msg' : message
    }
    return render(request, "edit_car.html", context)

@login_required
def delete_car_form(request, car_id):
    car = Car.objects.get(id = car_id)

    car.delete()
    return redirect(car_form)

@login_required
def staff_form(request):
    message = ''
    if request.method == 'POST':
        staffform = StaffForm(request.POST)

        if staffform.is_valid():
            staffform.save()
            return redirect('staff_page')

    else:
        staffform = StaffForm()

    staff = Staff.objects.all()
    context = {
        'form' : staffform,
        'msg' : message,
        'staff': staff
    }

    return render(request, 'staff.html', context)

@login_required
def edit_staff(request, staff_id):
    staff = Staff.objects.get(id = staff_id)
    message = ''

    if request.method == "POST":
        staffform = StaffForm(request.POST, instance=staff)

        if staffform.is_valid():
            staffform.save()
            return redirect('staff_page')

        else:
            message = "Form has invalid data"

    else:
        staffform = StaffForm(instance=staff)

    context = {
        'form': staffform,
        'msg': message,
        'staff': staff
    }
    return render(request, 'edit_staff.html', context)

@login_required
def delete_staff_form(request, staff_id):
    staff = Staff.objects.get(id = staff_id)

    staff.delete()
    return redirect(staff_form)

@login_required
def assign_form(request):
    message = ''
    if request.method == "POST":
        assignform = AssigningForm(request.POST)

        if assignform.is_valid():
            assignform.save()
            return redirect('assignment_page')

    else:
        assignform = AssigningForm()

    assign = Assigning.objects.all()

    context = {
        'form' : assignform,
        'msg' : message,
        'assign' : assign
    }
    return render(request, 'assignment.html', context)

@login_required
def edit_assignment(request, assignmentid):
    assignment = Assigning.objects.get(id = assignmentid)
    message = ''

    if request.method == 'POST':
        assignmentform = AssigningForm(request.POST, instance=assignment)

        if assignmentform.is_valid():
            assignmentform.save()
            return redirect('assignment_page')

        else:
            message = 'Form has invalid data'

    else:
        assignmentform = AssigningForm(instance=assignment)

    context = {
        'form' : assignmentform,
        'msg' : message,
        'assignment' : assignment
    }
    return render(request, "edit_assignment.html", context)


@login_required
def delete_assign_form(request, assign_id):
    assign = Assigning.objects.get(id = assign_id)

    assign.delete()
    return redirect(assign_form)

@login_required
def repair_issues_form(request):
    message = ''
    if request.method == "POST":
        repairissuesform = Repair_issuesForm(request.POST)

        if repairissuesform.is_valid():
            repairissuesform.save()
            return redirect('repair_issues_page')

    else:
        repairissuesform = Repair_issuesForm()

    repairissues = Repair_issues.objects.all()

    context = {
        'form' : repairissuesform,
        'msg' : message,
        'repairissues' : repairissues
    }
    return render(request, 'repairissues.html', context)


@login_required
def edit_repair_issues(request, repairissuesid):
    repairissues = Repair_issues.objects.get(id = repairissuesid)
    message = ''

    if request.method == 'POST':
        repairissuesform = Repair_issuesForm(request.POST, instance=repairissues)

        if repairissuesform.is_valid():
            repairissuesform.save()
            return redirect('repair_issues_page')

        else:
            message = 'Form has invalid data'

    else:
        repairissuesform = Repair_issuesForm(instance=repairissues)

    context = {
        'form' : repairissuesform,
        'msg' : message,
        'repairissues' : repairissues
    }
    return render(request, "edit_repair_issues.html", context)

@login_required
def delete_repair_issues_form(request, repair_issues_id):
    repair_issues = Repair_issues.objects.get(id = repair_issues_id)

    repair_issues.delete()
    return redirect(repair_issues_form)

@login_required
def edit_repair_records(request, repairrecordsid):
    repairrecords = Repair_records.objects.get(id = repairrecordsid)
    message = ''

    if request.method == 'POST':
        repairrecordsform = Repair_recordsForm(request.POST, instance=repairrecords)

        if repairrecordsform.is_valid():
            repairrecordsform.save()
            return redirect('repair_records_page')

        else:
            message = 'Form has invalid data'

    else:
        repairrecordsform = Repair_recordsForm(instance=repairrecords)

    context = {
        'form' : repairrecordsform,
        'msg' : message,
        'repairrecords' : repairrecords
    }
    return render(request, "edit_repair_records.html", context)

@login_required
def repair_records_form(request):
    message = ''
    if request.method == "POST":
        repairrecordsform = Repair_recordsForm(request.POST)

        if repairrecordsform.is_valid():
            repairrecordsform.save()
            return redirect('repair_records_page')

    else:
        repairrecordsform = Repair_recordsForm()

    repairrecords = Repair_records.objects.all()

    context = {
        'form' : repairrecordsform,
        'msg' : message,
        'repairrecords' : repairrecords
    }
    return render(request, 'repairrecords.html', context)

@login_required
def delete_repair_records_form(request, repair_records_id):
    repair_records = Repair_records.objects.get(id = repair_records_id)

    repair_records.delete()
    return redirect(repair_records_form)

@login_required
def service_issues_form(request):
    message = ''
    if request.method == "POST":
        serviceissuesform = Service_issuesForm(request.POST)

        if serviceissuesform.is_valid():
            serviceissuesform.save()
            return redirect('service_issues_page')

    else:
        serviceissuesform = Service_issuesForm()

    serviceissues = Service_issues.objects.all()

    context = {
        'form' : serviceissuesform,
        'msg' : message,
        'serviceissues' : serviceissues
    }
    return render(request, 'serviceissues.html', context)

@login_required
def delete_service_issues_form(request, service_issues_id):
    service_issues = Service_issues.objects.get(id = service_issues_id)

    service_issues.delete()
    return redirect(service_issues_form)

@login_required
def edit_service_records(request, servicerecordsid):
    servicerecords = Service_records.objects.get(id = servicerecordsid)
    message = ''

    if request.method == 'POST':
        servicerecordsform = Service_recordsForm(request.POST, instance=servicerecords)

        if servicerecordsform.is_valid():
            servicerecordsform.save()
            return redirect('service_records_page')

        else:
            message = 'Form has invalid data'

    else:
        servicerecordsform = Service_recordsForm(instance=servicerecords)

    context = {
        'form' : servicerecordsform,
        'msg' : message,
        'servicerecords' : servicerecords
    }
    return render(request, "edit_service_records.html", context)

@login_required
def delete_service_records_form(request, service_records_id):
    service_records = Service_records.objects.get(id = service_records_id)

    service_records.delete()
    return redirect(service_records_form)

@login_required
def edit_service_issues(request, serviceissuesid):
    serviceissues = Service_issues.objects.get(id = serviceissuesid)
    message = ''

    if request.method == 'POST':
        serviceissuesform = Service_issuesForm(request.POST, instance=serviceissues)

        if serviceissuesform.is_valid():
            serviceissuesform.save()
            return redirect('service_issues_page')

        else:
            message = 'Form has invalid data'

    else:
        serviceissuesform = Service_issuesForm(instance=serviceissues)

    context = {
        'form' : serviceissuesform,
        'msg' : message,
        'serviceissues' : serviceissues
    }
    return render(request, "edit_service_issues.html", context)

@login_required
def service_records_form(request):
    message = ''
    if request.method == "POST":
        servicerecordsform = Service_recordsForm(request.POST)

        if servicerecordsform.is_valid():
            servicerecordsform.save()
            return redirect('service_records_page')

    else:
        servicerecordsform = Service_recordsForm()

    servicerecords = Service_records.objects.all()

    context = {
        'form' : servicerecordsform,
        'msg' : message,
        'servicerecords' : servicerecords
    }
    return render(request, 'servicerecords.html', context)

@login_required
def fuelling_form(request):
    message = ''
    if request.method == "POST":
        fuelform = FuellingForm(request.POST)

        if fuelform.is_valid():
            fuelform.save()
            return redirect('fuelling_page')

    else:
        fuelform = FuellingForm()

    fuel = Fuelling.objects.all()

    context = {
        'form' : fuelform,
        'msg' : message,
        'fuel' : fuel
    }
    return render(request, 'fuel.html', context)

@login_required
def edit_fuel(request, fuelid):
    fuel = Fuelling.objects.get(id = fuelid)
    message = ''

    if request.method == 'POST':
        fuel_form = FuellingForm(request.POST, instance=fuel)

        if fuel_form.is_valid():
            fuel_form.save()
            return redirect('fuelling_page')

        else:
            message = 'Form has invalid data'

    else:
        fuel_form = FuellingForm(instance=fuel)

    context = {
        'form' : fuel_form,
        'msg' : message,
        'fuel' : fuel
    }
    return render(request, "edit_fuel.html", context)

@login_required
def delete_fuel_form(request, fuel_id):
    fuel = Fuelling.objects.get(id = fuel_id)

    fuel.delete()
    return redirect(fuelling_form)

def sign_up_view(request):
    message = ''
    if request.method == 'POST':
        sign_up_form = UserCreationForm(request.POST)

        if sign_up_form.is_valid():
            sign_up_form.save()
            return redirect(reverse('login') + '?signed_up=1')

        else:
            message = 'Please fix the errors below'

    else:
        sign_up_form = UserCreationForm()

    context = {
        'form' : sign_up_form,
        'msg': message
    }

    return render(request, 'registration/sign_up.html', context)
