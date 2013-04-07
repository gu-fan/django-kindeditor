from django import forms
from django.conf import settings

class KindWidget(forms.Textarea):
    """
    Setup the JS files and targetting CSS class for a textarea to
    use TinyMCE.
    """

    class Media:
        js = (settings.STATIC_URL + 'js/widgets/kindeditor.js',
              settings.STATIC_URL + 'js/widgets/init.js',)

    def __init__(self, *args, **kwargs):
        super(KindWidget, self).__init__(*args, **kwargs)
        self.attrs["class"] = "kind"

