from django import forms
from .models import Career, Application
from django.core.exceptions import ValidationError
from .validators import validate_email, PhoneValidator, validate_f_name, validate_date


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ('f_name', 'email', 'p_number', 'message')
        widgets = {
            'f_name': forms.TextInput(
                attrs={'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter', 'id': 'formGroupExampleInput',
                       'placeholder': 'Full Name',
                       'name': "f_name"}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter',
                       'id': 'formGroupExampleInput2', 'placeholder': 'Email',
                       'name': "email"}),
            'p_number': forms.TextInput(
                attrs={'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter',
                       'id': 'formGroupExampleInput3', 'placeholder': 'Phone Number',
                       'name': "p_number"}),
            'message': forms.Textarea(
                attrs={'class': 'form-control pt-3 pb-1 ps-4 font_fv font_style_b fw-lighter',
                       'id': 'floatingTextarea2', 'placeholder': 'Message',
                       'name': "message", 'style': {'height': '100px'}}),

        }

    def __init__(self, *args, **kwargs):
        super(CareerForm, self).__init__(*args, **kwargs)
        self.fields['f_name'].label = ""
        self.fields['email'].label = ""
        self.fields['p_number'].label = ""
        self.fields['message'].label = ""


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = (
            'parent_fname', 'parent_address', 'email', 'home_phone', 'cell_phone', 'child_fname',
            'date_of_birth',
            'child_address', 'child_img', 'child_text')
        widgets = {
            'parent_fname': forms.TextInput(
                attrs={'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter', 'id': 'formGroupExampleInput',
                       'placeholder': 'Parrent full name',
                       'name': "p_fname"}),
            'parent_address': forms.TextInput(
                attrs={'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter',
                       'id': 'formGroupExampleInput2',
                       'placeholder': 'Parrent address',
                       'name': "p_address"}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter',
                       'id': 'formGroupExampleInput3', 'placeholder': 'Email',
                       'name': "email"}),
            'home_phone': forms.TextInput(
                attrs={'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter',
                       'id': 'formGroupExampleInput4', 'placeholder': 'Home phone number',
                       'name': "h_number"}),
            'cell_phone': forms.TextInput(
                attrs={'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter',
                       'id': 'formGroupExampleInput5', 'placeholder': 'Cell phone number',
                       'name': "c_number"}),
            'child_fname': forms.TextInput(
                attrs={'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter',
                       'id': 'formGroupExampleInput6',
                       'placeholder': "Child's full name",
                       'name': "c_fname"}),
            # 'radio_yes': forms.CheckboxInput(
            #     attrs={'class': 'form-check-input', 'type': 'radio',
            #            'id': 'radio_yes', 'name': "yes_no"}),
            # "radio_no": forms.CheckboxInput(
            #     attrs={'class': 'form-check-input', 'type': 'radio',
            #            'id': 'radio_no', 'name': "yes_no"}),
            'date_of_birth': forms.DateInput(
                attrs={'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter',
                       'id': 'formGroupExampleInput8', 'placeholder': 'Date of Birth',
                       'name': "d_birth"}),
            'child_address': forms.TextInput(
                attrs={'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter',
                       'id': 'formGroupExampleInput9', 'placeholder': 'Child Address',
                       'name': "c_address"}),
            'child_img': forms.FileInput(
                attrs={'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter',
                       'id': 'formGroupExampleInput10', 'placeholder': "Child's Img",
                       'name': "c_img"}),
            'child_text': forms.Textarea(
                attrs={'class': 'form-control pt-3 pb-1 ps-4 font_fv font_style_b fw-lighter',
                       'id': 'floatingTextarea1', 'placeholder': 'Describe your child',
                       'name': "c_text"}),

        }

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['parent_fname'].label = ""
        self.fields['parent_address'].label = ""
        self.fields['email'].label = ""
        self.fields['home_phone'].label = ""
        self.fields['cell_phone'].label = ""
        self.fields['child_fname'].label = ""
        self.fields['date_of_birth'].label = ""
        self.fields['child_address'].label = ""
        self.fields['child_img'].label = ""
        self.fields['child_text'].label = ""


class ContactForm(forms.Form):
    f_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter',
                                      'id': 'formGroupExampleInput',
                                      'placeholder': 'Full Name'}),
        validators=[validate_f_name],
        label="",
        help_text="Required. The full name."
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter',
                                       'id': 'formGroupExampleInput2',
                                       'placeholder': 'Email'}),
        validators=[validate_email],
        label="",
        help_text="Required email address."
    )
    p_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter',
                                      'id': 'formGroupExampleInput3',
                                      'placeholder': 'Phone Number'}),
        validators=[PhoneValidator()],
        label="",
        help_text='Enter phone number e.g: +998123456789'
    )
    c_f_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter',
                                     'id': 'formGroupExampleInput4',
                                     'placeholder': "Child's full name"}),
        validators=[validate_f_name],
        label="",
        help_text="Required. The full name of the child."

    )
    c_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control py-3 ps-4 font_fv font_style_b Dateclass',
                                      'type': 'date',
                                      'id': 'formGroupExampleInput8',
                                      'placeholder': "Child's date of birth"}),
        validators=[validate_date],
        label="",
        help_text="Date format: dd/mm/yyyy"
    )
    a_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'Dateclass form-control py-3 ps-4 font_fv font_style_b',
                                      'type': 'date',
                                      'id': 'formGroupExampleInput9',
                                      'placeholder': "Anticipated start date"}),
        validators=[validate_date],
        label="",
        help_text="Date format: dd/mm/yyyy"
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control pt-3 pb-1 ps-4 font_fv font_style_b fw-lighter',
                                     'id': 'floatingTextarea10',
                                    }),
        label="",
        help_text="Enter your any message here."
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
