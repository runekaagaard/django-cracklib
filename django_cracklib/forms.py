from django.forms import forms
from django.contrib.auth.forms import SetPasswordForm
from django.utils.translation import ugettext as _
from django_cracklib.settings import DJANGO_CRACKLIB
from django.utils.safestring import mark_safe

class CracklibSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CracklibSetPasswordForm, self).__init__(*args, **kwargs)
     
    def clean(self):
        super(CracklibSetPasswordForm, self).clean()
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if None in (password1, password2):
            return
        
        try:
            import crack
            crack.VeryFascistCheck(password1, dictpath=DJANGO_CRACKLIB['dict_path'])
        except ValueError, message:
            if DJANGO_CRACKLIB['append_error_message']:
                extra = DJANGO_CRACKLIB['append_error_message']
            else:
                extra = u''
            raise forms.ValidationError, mark_safe("%s %s" % (_(str(message)), extra))
