from django import forms
from django.core.mail import mail_managers


SUBJECT_CHOICES = [
    ("general", "General Enquiry"),
    ("media", "Media / Press"),
    ("sponsorship", "Sponsorship"),
    ("grants", "Grants"),
    ("board", "Board & Governance"),
]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"autocomplete": "name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"autocomplete": "email"}))
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 6}))

    def send_email(self):
        data = self.cleaned_data
        subject = f"[DEFNA Contact] {dict(SUBJECT_CHOICES)[data['subject']]} from {data['name']}"
        body = f"From: {data['name']} <{data['email']}>\n\n{data['message']}"
        mail_managers(subject, body, fail_silently=True)
