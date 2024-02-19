from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from new_app.models import Register, Student, Admin, Marks


class RegistrationForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Register
        fields = ('username', 'password1', 'password2')


# for_date_of_birth
class DateInput(forms.DateInput):
    input_type = 'date'


class adminRegistrationForm(forms.ModelForm):
    contact_number = forms.CharField(max_length=10, validators=[RegexValidator(
        '^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$',
        message="Enter a valid Indian phone number")])

    class Meta:
        model = Admin
        fields = ('name', 'contact_number')


# student registration form
class studentRegistrationForm(forms.ModelForm):
    dob = forms.DateField(widget=DateInput)

    def clean_date(self):
        dob = self.cleaned_data['dob']
        if dob > datetime.date.today():
            raise forms.ValidationError("The date cannot be in future!")
        return dob

    contact_number = forms.CharField(max_length=10, validators=[RegexValidator(
        '^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$',
        message="Enter a valid Indian phone number")])

    def calculate_age(self):
        from datetime import date
        today = date.today()
        birth_date = self.dob
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age


    class Meta:
        model = Student
        fields = ('name', 'dob', 'contact_number', 'photo')


class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ('name','english', 'maths', 'science')
