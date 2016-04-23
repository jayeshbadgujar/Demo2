from django.conf.urls import url
from django.contrib import admin

from .views import (
	home,
	quotation_delete,
	quotation_list,
	updatequotation,
	delete_quotation,
	)

urlpatterns = [
	url(r'^$', home, name="home"),
	url(r'^quotation_delete/$', quotation_delete, name="quotation_delete"),
    url(r'^quotation_list/$', quotation_list, name="quotation_list"),
    url(r'^updatequotation/$', updatequotation, name="updatequotation"),
    url(r'^delete_quotation/(?P<pk>[0-9]+)/$', delete_quotation, name="delete_quotation"),

]