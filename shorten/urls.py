from django.conf.urls import patterns, include, url
from views import redirect, shorten

urlpatterns = patterns('',
    url(r'^shorten/', 'views.shorten'),
    url(r'', 'views.redirect'),
)
