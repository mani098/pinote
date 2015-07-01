from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from weblinks.models import WebLinks


@login_required
def weblinks_view(request):
	"""Fetches all the web links saved by a user"""

	records = WebLinks.objects.filter(user_id=request.user.id)
	json_response = [dict(title=record.title, url=record.url, description=record.description) for record in records]
	return JsonResponse(json_response, safe=False)
