About
=====

Django Cracklib adds password strength validation to the password reset confirm
form for django-registration. It also serves as a example to implement cracklib
with Python and/or Django.

Installation
============

Django registration
-------------------
Django Cracklib depends on the default backend of django-registration. Read all
about it here: http://django-registration.readthedocs.org/en/latest/index.html.

Cracklib
--------

The cracklib python library can be found at 
http://pypi.python.org/pypi/cracklib.

On Ubuntu installing is as simple as::

    sudo apt-get install python-cracklib

Django Cracklib
---------------

Clone the source somewhere on Djangos python path::

    git clone git://github.com/runekaagaard/django-cracklib.git

Add "django_cracklib" to INSTALLED_APPS in settings.py. Add an entry in urls.py
similar to::

	from django.contrib.auth.views import password_reset_confirm
	from django_cracklib.forms import CracklibSetPasswordForm
	
	urlpatterns = patterns('',
		# Other patterns here.
		
		(r'^account/password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)$', 
     	 password_reset_confirm, {'set_password_form': CracklibSetPasswordForm}),
    ) 
The following settings is available::

    DJANGO_CRACKLIB = {
		# The absolute path to the wordlist file or directory.
		'dict_path': '/var/cache/cracklib/cracklib_dict',
		# Optional template path, to render the error message. The variable
		# {{message}} is provided for the template.
		'error_message_template': None,
	}

Installing the cracklib library
===============================

Install cracklib and wordlists with banned words by following the guide at
http://www.2sheds.ru/blog/2007/03/generate-cracklib-word-library-on-ubuntu-linux/.

Two examples of additional wordlists:

- http://www.openwall.com/passwords/wordlists/password-2011.lst
- http://www.cotse.com/wordlists/common-p

Translation
===========

Translations can be downloaded in .po format at
https://translations.launchpad.net/ubuntu/precise/+source/cracklib2/+pots/cracklib.
A modified danish translation is included.

Copy the .po file to 
"django_cracklib/locale/[LANGUAGE_CODE]/LC_MESSAGES/django.po".

To recompile the messages cd to "django_cracklib" and run::

	django-admin.py compilemessages
	
Known bugs
==========

If you get a segfault like in
http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=596281, a fast solution is
to set the "dict_path" setting to None, so it won't be passed to cracklib which
is what causes the bug. You need to be sure that the dictionary files is
available at the default location that cracklib expects on your system. On
ubuntu 10.10 it just worked when following the guide, but I don't know how to 
get the default location on other systems. Another solution is to update to the 
latest version, but on ubuntu that requires Python 2.7 too. You can run the
"test_cracklib.py" script to see if this bug affects you. 