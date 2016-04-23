
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Quotation(models.Model):
	client = models.CharField(max_length=100)
	qotat_no = models.IntegerField(unique=True)

	def __unicode__(self):
		return unicode(self.qotat_no)

class Item(models.Model):
	qotat_no = models.ForeignKey(Quotation)
	name1 = models.CharField(max_length=100)
	name2 = models.CharField(max_length=100)
	quantity = models.IntegerField()
	price = models.FloatField()
	total = models.FloatField()
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return self.name2

	def save(self, *args, **kwargs):
		super(Item, self).save(*args, **kwargs)
		slug = slugify(self.name)
		self.slug = "%s-%s" %(slug, self.pk)
		super(Item, self).save(*args, **kwargs)


	def get_absolute_url(self):
		return reverse("quotation:update", kwargs={"slug": self.slug})