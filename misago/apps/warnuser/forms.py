from django.utils.translation import ugettext_lazy as _
import floppyforms as forms
from misago.forms import Form

class WarnMemberForm(Form):
    reason = forms.CharField(label=_("Warning Reason"), max_length=2048,
                             widget=forms.Textarea,
                             error_messages={'max_length': _("Warn reason is too long.")})
