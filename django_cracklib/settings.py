from django.conf import settings

DJANGO_CRACKLIB = {
	# The absolute path to the wordlist file or directory.
	'dict_path': '/var/cache/cracklib/cracklib_dict',
	# Optional template path, to render the error message. The variable
	# {{message}} is provided for the template.
	'error_message_template': None,
}

try:
	DJANGO_CRACKLIB.update(settings.DJANGO_CRACKLIB)
except AttributeError:
	pass