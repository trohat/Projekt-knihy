from django import forms

from .models import Kniha

# class KnihaForm(forms.Form):
#     jmeno = forms.CharField(label="Jméno knihy:", max_length=20, error_messages={
#         "required": "Kniha musí mít název!",
#         "max_length": "Název je moc dlouhý."
#     })
#     autor = forms.CharField(max_length=200, error_messages={
#         "required": "Kniha musí mít autora!"
#     })
#     rok = forms.IntegerField(label="Rok vydání:")

class KnihaForm(forms.ModelForm):
    class Meta:
        model = Kniha
        fields = "__all__" # tohle spíše nepoužívejte, už víte proč

        labels = {
            "jmeno": "Jméno knihy",
            "rok": "Rok vydání"
        }

        error_messages = {
            "jmeno": {
                "required": "Jméno knihy je povinné.",
                "max_length": "Jméno knihy je moc dlouhé."
            },
            "autor": {
                "required": "Jméno autora je povinné."
            }
        }