from django.conf.urls import patterns, include, url
import shorten.views

urlpatterns = patterns('',
    url(r'shorten/$', 'shorten.views.shorten'),
    url(r'shorten$', 'shorten.views.shorten'),
    url(r'(?P<query>\w+)', 'shorten.views.redirect'),
)
