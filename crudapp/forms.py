from django import forms

class Employee_form(forms.Form):
	eid = forms.CharField(max_length=20)
	ename = forms.CharField(max_length=20)
	eemail = forms.EmailField()
	econtact = forms.CharField(max_length=12)