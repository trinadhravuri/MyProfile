from django import forms
from .models import Enquiry
from django.forms import widgets



class EnquiryForm(forms.ModelForm):

    class Meta:
        model = Enquiry
        fields = '__all__'

    def __init__(self, *args,**kwaargs):
        super(EnquiryForm,self).__init__(*args, **kwaargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['contact'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['message'].widget.attrs.update({'class':'form-control'})