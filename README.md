#Django URL Shortener

Yet another URL shortener written in Python using Django framework.

##API
`POST /shorten`
<br>Parameters: Parameter link contains the link to shorten.
<br>Returns: Id for the shortened link in text/plain format.

`GET /{id}`
<br>Returns: 301 redirects the user agent to a previously stored URL. 404 error if no link stored with given id.
