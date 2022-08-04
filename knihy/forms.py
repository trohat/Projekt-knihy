from django import forms

class KnihaForm(forms.Form):
    jmeno = forms.CharField(label="Jméno knihy:", max_length=20, error_messages={
        "required": "Kniha musí mít název!",
        "max_length": "Název je moc dlouhý."
    })
    autor = forms.CharField(max_length=200, error_messages={
        "required": "Kniha musí mít autora!"
    })
    rok = forms.IntegerField(label="Rok vydání:")

    