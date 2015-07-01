from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse


def login_view(request):

	if request.user.is_authenticated():
		return HttpResponseRedirect('/home/')
	else:
		# If the request is a HTTP POST, try to pull out the relevant information.
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			# Use Django's machinery to attempt to see if the username/password
			# combination is valid - a User object is returned if it is.
			user = authenticate(username=username, password=password)
			if user:
				# Is the account active? It could have been disabled.
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect("/home/")

				else:
					# An inactive account was used - no logging in!
					return HttpResponse("Your Pinote account is disabled.")
			else:
				print "Invalid login details: {0}, {1}".format(username, password)
				return HttpResponse("Invalid login details supplied.")

		# The request is not a HTTP POST, so display the login form.
		# This scenario would most likely be a HTTP GET.
		else:
			# No context variables to pass to the template system, hence the
			# blank dictionary object...
			return render(request, 'login.html', {})


@login_required
def home_view(request):
	return HttpResponse(open("./templates/base.html").read())


@login_required
def get_user(request):
	return HttpResponse(request.user.username)


@login_required
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
