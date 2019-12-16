from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from .forms import UserForm,RecordForm
from .models import django_model
from .conn import connect_psql,request_record_id

def index(request):
	return render(request,'mydjangoapp/index.html',{})

def about_us(request):
	return render(request,'mydjangoapp/about_us.html',{})

def contact_us(request):
	first_name=''
	last_name=''
	email=''

	form= UserForm(request.POST or None)
	if form.is_valid():
	       	first_name= form.cleaned_data.get("first_name")
	        last_name= form.cleaned_data.get("last_name")
        	email= form.cleaned_data.get("email")

	return render(request,'mydjangoapp/contact_us.html',{'form': form})

def thank_you(request):
	form = UserForm()
	record_id = ''

	if request.method == "POST":
		# print("POST")
		form = UserForm(request.POST)

		if form.is_valid():
			data = form.save(commit=False)
			record_id = connect_psql(data.first_name,data.last_name,data.email)
			#print(record_id)
			data.save()

	elif request.method == "GET":
		print("GET")
	else:
		form = UserForm()


	context= {'id':record_id}
	print(context['id'])
	#return render(request,'mydjangoapp/check.html',context)

	return render(request,'mydjangoapp/thank_you.html',context)

def check(request):
	submitbutton= request.POST.get("submit")
	form = RecordForm()
	id = ''
	first_name=''
	last_name=''
	email=''

	request_id = ''
	request_firstname = ''
	request_lastname = ''
	request_email = ''

	if request.method == "POST":
		print("POST")
		form = RecordForm(request.POST)

		if form.is_valid():
			data = form.cleaned_data.get("id")
			keys_record_id = request_record_id(data)
			if keys_record_id is None:
				print("RecordID is not exist")
				request_id = None
				request_firstname = None
				request_lastname = None
				request_email = None
				context= {'form': form,'id':request_id,'first_name':request_firstname,'last_name':request_lastname,'submitbutton': submitbutton,'email':request_email}
				return render(request,'mydjangoapp/check.html',context)


				
			request_id =  keys_record_id[0]
			request_firstname = keys_record_id[1]
			request_lastname = keys_record_id[2]
			request_email = keys_record_id[3]


	elif request.method == "GET":
		print("GET")
	else:
		form = RecordForm()

	context= {'form': form,'id':request_id,'first_name':request_firstname,'last_name':request_lastname,'submitbutton': submitbutton,'email':request_email}
	return render(request,'mydjangoapp/check.html',context)


