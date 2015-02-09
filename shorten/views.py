import urllib2
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect as http_redirect
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseBadRequest
from shorten.models import Url
from shorten.conversions import convert_to_base62, convert_from_base62
from datetime import datetime
from django.http import Http404
from urlparse import urlparse

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
		#TODO do we enforce this?
		print "Not application/x-www-form-urlencoded"

	submitted_url = request.POST.get('link')
	if submitted_url == None or len(submitted_url) == 0:
		return HttpResponseBadRequest("No url specified.")

	#Make sure we have a scheme for the url. Else add http as default.
	url_parsed = urlparse(submitted_url.strip())
        if url_parsed.scheme == '':
            submitted_url = "http://"+ submitted_url
	print "Shorten request:", submitted_url

	#Check if we already have already shortened this URL
	url = None

	try:
		url = Url.objects.get(url=submitted_url)
	except Url.DoesNotExist:
		print "New Url"

	if url != None:
		#We already have a shortened url for the given url
		return HttpResponse(convert_to_base62(url.id))

	url = Url()
	url.url = submitted_url
	url.date_created = datetime.now()
	url.save()
	return HttpResponse(convert_to_base62(url.id))