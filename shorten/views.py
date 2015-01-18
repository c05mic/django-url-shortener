from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect as http_redirect
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponsePermanentRedirect
from shorten.models import Url
from shorten.conversions import convert_to_base62, convert_from_base62
from datetime import datetime
from django.http import Http404

def redirect(request, query):
	print query
	id = convert_from_base62(query)
	if id < 0:
		#Unknown shortened url
		raise Http404("Url does not exist")

	url = get_object_or_404(Url, id=id)
	return HttpResponsePermanentRedirect(url.url)

@require_http_methods(["POST"])
def shorten(request):
	if request.META.get('CONTENT_TYPE') != "application/x-www-form-urlencoded":
		#TODO do we need to enforce this?
		print "Not application/x-www-form-urlencoded"

	submitted_url = request.POST.get('link')
	print "Shorten request:", submitted_url

	#Check if we already have already shortened this URL
	#url = Url.objects.get(url=submitted_url)

	#if url != None:
		#We already have a shortened url for the given url
	#	return HttpResponse(url.id)

	url = Url()
	url.url = submitted_url
	url.date_created = datetime.now()
	url.save()
	return HttpResponse(url.id)