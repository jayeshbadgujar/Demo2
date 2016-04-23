from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import Item, Quotation
from .forms import DeleteItem, QuotationForm, ItemForm



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
				n = Item.objects.get(qotat_no=qotat_no)
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
		item = Item.objects.get(pk=pk)
		item.delete()
		return HttpResponseRedirect('/quotation/item_delete/')
	except:
		return HttpResponse("user does not match. or update does not exist.")


def quotation_list(request):
  context = {}
  item_list = Item.objects.all()
  print item_list

  context["item_list"] = item_list  
  return render(request, "quotation/item_list.html", context)

def updatequotation(request):
    context={}
    if request.method == 'POST':
        user_form = ItemForm(data = request.POST)
        if user_form.is_valid():
            qotat_no = request.POST.get('qotat_no')
            name1 = request.POST.get('name1')
            name2 = request.POST.get('name2')
            quantity = request.POST.get('quantity')
            price = request.POST.get('price')
        try:
        	n = Item.objects.get(qotat_no=qotat_no)
        	n = Item.objects.get(name1=name1)
	        Item.objects.filter(qotat_no=qotat_no).update(
	            name2=name2,
	            quantity=quantity,
	            price=price,
	            )   
	        return HttpResponseRedirect('/quotation/updateitem/')
        except:
        	return HttpResponse("Item name is not match")
        else:
        	return HttpResponse("form is not valid")
    else:
        user_form = ItemForm()

    context={'user_form':user_form}
    return render (request,'quotation/update.html',context)