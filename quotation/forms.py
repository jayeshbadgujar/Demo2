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
		fields = ['qotat_no', 'name', 'quantity', 'price']
		widgets = {
			'qotat_no': forms.TextInput(attrs={ 'required': 'required' }),
			'name': forms.TextInput(attrs={ 'required': 'required' }),
			'quantity': forms.TextInput(attrs={ 'required': 'required' }),
			'price': forms.TextInput(attrs={ 'required': 'required' }),

	}


def add_update_ad(request, pk=None):
    if pk is not None:
        instance = Item.objects.get(pk=pk)
    else:
        instance = Item()

    if request.POST:
        form = ItemForm(request.POST, instance=instance)
        if form.is_valid():
            new_instance = form.save()
            return HttpResponseRedirect('my_confirmation_view')
    else:
        form = ItemForm(instance=instance)
    return render(request, 'quotation/update.html', {'form': form})