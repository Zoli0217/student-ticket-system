from django import forms

class TicketForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))