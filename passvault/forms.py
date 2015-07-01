from django import forms
from models import PassVault


class SavePassvaultForm(forms.ModelForm):
	class Meta:
		model = PassVault
		fields = ('name', 'password', 'description')
