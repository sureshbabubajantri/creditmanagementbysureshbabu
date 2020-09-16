from django import forms
from .models import Add_User_Model,Transfer_Table_Model
class Add_User_Form(forms.ModelForm):
	"""docstring for Add_User_Form"""
	class Meta:
		model=Add_User_Model
		fields=['name','credit_amount']
class Transfer_Table_Form(forms.ModelForm):
	class Meta:
		model=Transfer_Table_Model
		fields=[]