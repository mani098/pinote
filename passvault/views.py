import json
# import time
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from passvault.models import PassVault
from forms import SavePassvaultForm


@login_required
def passvault_view(request):
	"""fetches all the user credentials stored in DB"""

	# time.sleep(5)
	records = PassVault.objects.filter(user_id=request.user.id)
	categories = [record.category for record in records if record.category]
	categories = list(set(categories))
	json_response = []

	for category in categories:  # loop for datas which has category
		category_data = []
		for record in records:
			if record.category == category:
				category_data.append(dict(id=record.id, name=record.name, password=record.password,
							custom_fields=record.custom_fields, description=record.description))
		json_response.append(dict(category=category, category_data=category_data))

	category_data = []
	for record in records:
		if not record.category:
			print record.id
			category_data.append(dict(id=record.id, name=record.name, password=record.password,
						custom_fields=record.custom_fields, description=record.description))
	json_response.append(dict(category="default", category_data=category_data))
	return JsonResponse(json_response, safe=False)


@login_required
def passvault_form_update(request):
	"""Saves the form data in db"""

	if request.method == 'POST':
		# print request.POST
		passvault_form = SavePassvaultForm(data=request.POST)
		passvault_dict = dict(request.POST.iterlists())
		if passvault_form.is_valid():
			record = PassVault.objects.get(id=passvault_dict["id"][0])
			if record:
				record.user_id = request.user.id
				record.name = passvault_dict["name"][0]
				record.password = passvault_dict["password"][0]
				record.category = passvault_dict["category"][0]
				record.custom_fields = json.loads(passvault_dict["custom_fields"][0])
				record.description = passvault_dict["description"][0]
				record.save()
			else:
				passvault_data = passvault_form.save(commit=False)
				# passvault_data.custom_fields = request.POST.custom_fields
				passvault_data.user_id = request.user.id
				passvault_data.save()
			return HttpResponse("data saved")
		else:
			print passvault_form.errors
			return "error occured while saving passvault fields"
	else:
		return HttpResponse("Not a post request")
