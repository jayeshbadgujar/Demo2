from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import Item, Quotation
from .forms import QuotationForm, ItemForm, DeleteItem
from django.forms import formset_factory


def home(request):
	return HttpResponse("Hi....Hello")

def quotation_delete(request):
	context = {}
	item_list = Item.objects.all()
	qotat_no = request.POST.get('qotat_no')
	if request.method == "POST":
		form = DeleteItem(request.POST)
		if form.is_valid():
			try:
				n = Item.objects.all()
				n.delete()
				print "hi"
				return HttpResponseRedirect('/')
			except Item.DoesNotExist:
				return HttpResponse("Item name not match. Plz check item name ")
		else:
			HttpResponse("form is not valid")
	else:
		form = DeleteItem()

	return render(request, "quotation/item_delete.html", { 'form': form, 'item_list': item_list })

def delete_quotation(request, pk):
	try:
		quotation = Quotation.objects.get(pk=pk)
		quotation.delete()
		return HttpResponseRedirect('/quotation/quotation_delete/')
	except:
		return HttpResponse("user does not match. or update does not exist.")


def quotation_list(request):
  context = {}
  item_list = Item.objects.all()
  print item_list

  context["item_list"] = item_list  
  return render(request, "quotation/item_list.html", context)

def update_quotation(request):
    context={}
    ItemFormSet = formset_factory(ItemForm)
    if request.method == 'POST':
        item_formset = ItemFormSet(data=request.POST)
        if item_formset.is_valid():
			qotat_no = request.POST.get('qotat_no')
			name = request.POST.get('name')
			quantity = request.POST.get('quantity')
			price = request.POST.get('price')
        try:
        	n = Item.objects.get(qotat_no=qotat_no, name=name)
	        Item.objects.filter(qotat_no=qotat_no, name=name).update(
	            name=name,
	            quantity=quantity,
	            price=price,
	            )   
	        return HttpResponseRedirect('/quotation/updateitem/')
        except:
        	print item_formset
        	return HttpResponse("Item name is not match")
        else:
        	return HttpResponse("form is not valid")
    else:
        item_formset = ItemFormSet()

    context={'item_formset':item_formset}
    return render (request,'quotation/update.html',context)