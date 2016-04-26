
from django.db import models
from django.utils.text import slugify
from django.forms import ModelForm

# Create your models here.
class Quotation(models.Model):
	client = models.CharField(max_length=100)
	qotat_no = models.IntegerField(unique=True)

	def __unicode__(self):
		return unicode(self.qotat_no)

class Item(models.Model):
	qotat_no = models.ForeignKey(Quotation)
	name = models.CharField(max_length=100)
	quantity = models.IntegerField()
	price = models.FloatField()
	total = models.FloatField()
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		super(Item, self).save(*args, **kwargs)
		slug = slugify(self.qotat_no)
		self.slug = "%s-%s" %(slug, self.pk)

		if self.quantity and self.price:
			self.total = self.quantity * self.price
			
		super(Item, self).save(*args, **kwargs)




	def get_absolute_url(self):
		return reverse("quotation:update", kwargs={"slug": self.slug})