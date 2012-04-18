from django.conf import settings

DJANGO_CRACKLIB = {
	# The absolute path to the wordlist file or directory.
	'dict_path': '/var/cache/cracklib/cracklib_dict',
	# HTML appended after the error message like "Whats the meaning of this?".
	'append_error_message': None,
}

try:
	DJANGO_CRACKLIB.update(settings.DJANGO_CRACKLIB)
except AttributeError:
	pass