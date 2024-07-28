from django import forms

class NameForm(forms.Form):
    link = forms.CharField(label="Link", max_length=100)


class NameForm2(forms.Form):
    def __init__(self, *args, **kwargs):
        # Extrair o parâmetro 'choices' do kwargs
        choices = kwargs.pop('choices', [])
        super().__init__(*args, **kwargs)  # Chama o __init__ da superclasse
        self.fields['my_field'] = forms.ChoiceField(
            choices=choices,
            widget=forms.Select(attrs={'class': 'form-control'})
        )

    