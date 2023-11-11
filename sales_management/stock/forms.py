from django import forms
from .models import products





# creating a form
class proform(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = products

		# specify fields to be used
		fields = [
			"name",
			"price",
			"quantity",
		]
