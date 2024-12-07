from django import forms
from StucturalTechExpertsapp.models import Quote, Contact


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'