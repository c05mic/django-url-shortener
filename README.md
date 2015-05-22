#Django URL Shortener

Yet another URL shortener written in Python using Django framework. 

__Status:__
[![Codacy Badge](https://www.codacy.com/project/badge/3a1ad454fc31435880213eb516cd6e77)](https://www.codacy.com/app/srsridhar5/django-url-shortener)

A detailed background for this project is at: [Django URL Shortener](https://c05mic.wordpress.com/2015/02/10/implementing-an-url-shortener-using-djangopython/)

##API
`POST /shorten`
<br>Parameters: Parameter link contains the link to shorten.
<br>Returns: Id for the shortened link in text/plain format.

`GET /{id}`
<br>Returns: 301 redirects the user agent to a previously stored URL. 404 error if no link stored with given id.
