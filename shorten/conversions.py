import math

ALLOWED_ALPHABETS = [
	'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
	't','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L',
	'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5',
	'6','7','8','9','0'
]

string_to_digit_map = {}

ctr = 0
for alpha in ALLOWED_ALPHABETS:
	string_to_digit_map[alpha] = ctr
	ctr = ctr + 1

def convert_to_base62(id):
	base62_string = ''
	while id > 0:
		rem = id % 62
		id = id / 62
		base62_string = ALLOWED_ALPHABETS[rem] + base62_string
	return base62_string

def convert_from_base62(string):
	res = 0
	digit_ctr = len(string) - 1
	for char in string:
		if char not in string_to_digit_map:
			return -1
		res = res + string_to_digit_map[char] * int(math.pow(62, digit_ctr))
		digit_ctr = digit_ctr - 1
	return res