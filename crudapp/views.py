from django.shortcuts import render,HttpResponse 
from django.http import HttpResponseRedirect
from .models import Employee
from .forms import Employee_form

# Create your views here.
def emp(request):
	if request.method =='POST':
		form = Employee_form(request.POST)

		if form.is_valid():
			Eid = form.cleaned_data['eid']
			Ename = form.cleaned_data['ename']
			Eemail = form.cleaned_data['eemail']
			Econtact = form.cleaned_data['econtact']

			e = Employee(eid=Eid,ename=Ename,eemail=Eemail,econtact=Econtact)
			e.save()

			return HttpResponseRedirect('/Home/show/')


			# employee = Employee.objects.all()
			# p = list(employee)
			# return render(request,'show.html',{'p': p})


	else:
		form = Employee_form()

	return render(request,'index.html',{'form':form})


def show(request):
	employee = Employee.objects.all()
	p = list(employee)
	return render(request,'show.html',{'p': p})

# def edit(request,id):
# 	Employee = Employee.objects.all(id=id)
# 	return render(request,'edit.html',{'employee':Employee})

def update(request,id):
	# import pdb;pdb.set_trace()
	emp = Employee.objects.get(id=id)

	if request.method == 'POST':
		form = Employee_form(request.POST)

		if form.is_valid():

			emp.eid = form.cleaned_data['eid']
			emp.ename = form.cleaned_data['ename']
			emp.eemaill = form.cleaned_data['eemail']
			emp.econtact = form.cleaned_data['econtact']
			emp.save()
			return HttpResponseRedirect('/Home/show/')

	else:

		data = {'eid':emp.eid,'ename':emp.ename,'eemail':emp.eemail,'econtact':emp.econtact}
		form = Employee_form(initial=data)


	return render(request,'edit.html',{'form':form})

#def update(request,id,template_name = 'edit.html')


def delete(request,id):
	Employee.objects.get(id=id).delete()
	
	return HttpResponseRedirect('/Home/show/')
