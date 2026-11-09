from django.forms import ModelForm
from .models import Car, Staff, Assigning,Fuelling, Repair_issues, Repair_records, Service_issues, Service_records

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

class AssigningForm(ModelForm):
    class Meta:
        model = Assigning
        fields = '__all__'  

class FuellingForm(ModelForm):
    class Meta:
        model = Fuelling
        fields = '__all__' 

class Repair_issuesForm(ModelForm):
    class Meta:
        model = Repair_issues
        fields = '__all__'

class Repair_recordsForm(ModelForm):
    class Meta:
        model = Repair_records
        fields = '__all__'

class Service_issuesForm(ModelForm):
    class Meta:
        model = Service_issues
        fields = '__all__'

class Service_recordsForm(ModelForm):
    class Meta:
        model = Service_records
        fields = '__all__'