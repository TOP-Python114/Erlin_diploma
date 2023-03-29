from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

my_default_errors = {
    'required': 'This field is required',
    'invalid': 'Enter a valid value'
}


class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField()
    error_messages = {
        'password_mismatch': "Пароли не совпадают",
        'username': "уже есть",

    }

    translate_ = {
        "A user with that username already exists.": "юзер уже есть"
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = "150 < симв. Только буквы, цифры и @/./+/-/_."
        self.fields['password1'].help_text = ['Ваш пароль должен быть больше 8 символов', 'Не состоять из одних цифр','Волосатая горилла']
        self.fields['password2'].help_text = None
        self.fields['password1'].label = "Введите пароль"  #   'placeholder': 'парольrgdfgdf','class': 'input_c'
        self.fields['password2'].label = "Повторите пароль"

        self.fields['password1'].widget = forms.PasswordInput(attrs={
          'placeholder': 'пароль','class': 'input_reg'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'placeholder': 'пароль еще раз','class': 'input_reg'
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'email': 'Введите почту',
            'username': 'Введите имя',

        }

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Имя', 'class':'input_reg'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'name@domain.[xx]', 'class':'input_reg'
            }),

        }
