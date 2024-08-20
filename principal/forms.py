from django import forms
from principal.models import Reserva
from principal.models import Producto
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password', 'email')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return confirm_password

ESTADOS = [
    ('reservada', 'RESERVADA'),
    ('completada', 'COMPLETADA'),
    ('anulada', 'ANULADA'),
    ('noAsisten', 'NO ASISTEN')
]

class FormularioReservas(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

    estado = forms.ChoiceField(choices=ESTADOS, widget=forms.Select(attrs={'class': 'form-control'}))
    observacion = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    estilista = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha = forms.DateTimeField(widget=forms.widgets.DateTimeInput(
        attrs={
            'type': 'datetime-local',
            'placeholder': 'yyyy-mm-ddThh:mm (Fecha y hora)',
            'class': 'form-control'
        }
    ))

class FormularioProductos(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

    estado = forms.ChoiceField(choices=ESTADOS, widget=forms.Select(attrs={'class': 'form-control'}))
    observacion = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    marca = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha = forms.DateTimeField(widget=forms.widgets.DateTimeInput(
        attrs={
            'type': 'datetime-local',
            'placeholder': 'yyyy-mm-ddThh:mm (Fecha y hora)',
            'class': 'form-control'
        }
    ))

class ActualizarReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'fono', 'fecha', 'estilista', 'estado', 'observacion']

    fecha = forms.DateTimeField(widget=forms.widgets.DateTimeInput(
        attrs={
            'type': 'datetime-local',
            'placeholder': 'yyyy-mm-ddThh:mm (Fecha y hora)',
            'class': 'form-control'
        }
    ))
