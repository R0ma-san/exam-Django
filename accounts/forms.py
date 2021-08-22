from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(max_length=30)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        
        if not User.objects.filter(username=username).exists:
            raise forms.ValidationError(f'Пользователь с логином {username} не найден!')
        user = User.objects.filter(username=username).first()
        
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль!')
        
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    def __init__(self, *args, **kwarqs):
        super().__init__(*args, **kwarqs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердите пароль'
        self.fields['phone'].label = 'Телефон'
        self.fields['email'].label = 'Электронная почта'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилие'

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Почтовый адрес уже зарегегистрирован!')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже зарегегистрирован!')
        return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password!=confirm_password:
            raise forms.ValidationError('Пароли не совпадают!')
        return self.cleaned_data

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password', 'confirm_password']