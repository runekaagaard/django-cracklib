from django.forms import forms
from django.contrib.auth.forms import SetPasswordForm
from django.utils.translation import ugettext as _
from django_cracklib.settings import DJANGO_CRACKLIB as CRACKLIB
from django.utils.safestring import mark_safe
from django.template import loader, Context

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
            crack.VeryFascistCheck(password1, dictpath=CRACKLIB['dict_path'])
            return self.cleaned_data
        except ValueError, message:
            message = _(str(message))
            if CRACKLIB['error_message_template']:
                t = loader.get_template(CRACKLIB['error_message_template'])
                output = t.render(Context({'message': message}))
            else:
                output = message
            raise forms.ValidationError, mark_safe(output)