from django import forms
from django.utils.translation import ugettext_lazy as _
from misago.timezones import tzlist
from misago.forms import Form


class UserForumOptionsForm(Form):
    newsletters = forms.BooleanField(required=False)
    timezone = forms.ChoiceField(choices=tzlist())
    hide_activity = forms.ChoiceField(choices=(
                                               (0, _("Show my presence to everyone")),
                                               (1, _("Show my presence to people I follow")),
                                               (2, _("Show my presence to nobody")),
                                               ))
    
    layout = (
              (
               _("Forum Options"),
               (
                ('hide_activity', {'label': _("Your Visibility"), 'help_text': _("If you want to, you can limit other members ability to track your presence on forums.")}),
                ('timezone', {'label': _("Your Current Timezone"), 'help_text': _("If dates and hours displayed by forums are inaccurate, you can fix it by adjusting timezone setting.")}),
                ('newsletters', {'label': _("Newsletters"), 'help_text': _("On occasion board administrator may want to send e-mail message to multiple members."), 'inline': _("Yes, I want to subscribe forum newsletter")}),
                )
               ),
              )