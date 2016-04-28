from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import Item, Quotation
from .forms import QuotationForm, ItemForm, DeleteItem, AutoCompleteOrderedItemForm
from django.forms import formset_factory
from django.template.context import RequestContext

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
	# OrderedItemFormset = get_ordereditem_formset(ItemForm, extra=1, can_delete=True)
	order = Item.objects.all()[0]
	if request.method == 'POST':
		formset = ItemForm(request.POST, instance=order)
		# formset = OrderedItemFormset(request.POST, instance=order)
		if formset.is_valid():
			# form.save()
			formset.save()
			return HttpResponseRedirect('/quotation/quotation_list/')
	else:
		formset = ItemForm(instance=order)
		# formset = OrderedItemFormset(instance=order)

	context={'formset': formset}
	return render (request,'quotation/update.html',context, context_instance=RequestContext(request))
