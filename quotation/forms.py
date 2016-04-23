from django import forms
from quotation.models import Item,  Quotation




class DeleteItem(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['qotat_no']
		widgets = {
			'qotat_no': forms.TextInput(attrs={ 'required': 'required' }),
	}

class QuotationForm(forms.ModelForm):
	class Meta:
		model = Quotation
		fields = ['client']
		widgets = {
			'client': forms.TextInput(attrs={ 'required': 'required' }),

	}


class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['qotat_no', 'name1', 'name2', 'quantity', 'price', 'slug']
		widgets = {
			'qotat_no': forms.TextInput(attrs={ 'required': 'required' }),
			'name1': forms.TextInput(attrs={ 'required': 'required' }),
			'name2': forms.TextInput(attrs={ 'required': 'required' }),
			'quantity': forms.TextInput(attrs={ 'required': 'required' }),
			'price': forms.TextInput(attrs={ 'required': 'required' }),

	}


