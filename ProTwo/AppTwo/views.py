from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Users
from AppTwo.forms import NewUser


def index(request):
	mydict = {'inserted_by_django': "Yea yea fine i came from django ....now pls shutup"}
	return render(request,'ProTwo/index.html',context=mydict)

def users(request):
	user_order = Users.objects.order_by('first_name')
	user_list = {'users_list' : user_order}
	return render(request,'ProTwo/users.html',context = user_list)

def signup(request):

	form = NewUser()

	if request.method == "POST":
		form = NewUser(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return index(request)

		else:
			print("Error FORM INVALID")

	return render(request,'ProTwo/signup.html',{'form':form})
