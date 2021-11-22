from django.forms import ModelForm
from .models import Customer,Info


class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'

class InfoForm(ModelForm):
	class Meta:
		model = Info
		fields = '__all__'


class formInfo(ModelForm):
	class Meta:
		model = Info
		fields = ['age','height','weight']