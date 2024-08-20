from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, correo, usuario=None, password=None, fecha_nacimiento=None, nombre=None, apellido=None, rut=None, admin=False, tecnico=False, activo=True):
        if not correo:
            raise ValueError('El usuario debe tener un correo')
        if not usuario:
            raise ValueError('El usuario debe tener un nombre de usuario')
        user = self.model(
            correo=self.normalize_email(correo),
            usuario=usuario,
            nombre=nombre,
            apellido=apellido,
            rut=rut,
            fecha_nacimiento=fecha_nacimiento,
        )
        user.set_password(password)
        user.admin = admin
        user.tecnico = tecnico
        user.activo = activo
        user.save()
        return user

    def create_superuser(self, correo, usuario, password=None):
        user = self.create_user(
            correo,
            usuario=usuario,
            password=password
        )
        user.admin = True
        user.save()
        return user

class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    rut = models.CharField(max_length=12, unique=True)
    correo = models.EmailField(max_length=70, unique=True)
    usuario = models.CharField(max_length=50, unique=True)
    fecha_nacimiento = models.DateField(null=True)
    activo = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    tecnico = models.BooleanField(default=False)
    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['correo', 'rut']

    def get_full_name(self):
        return f"{self.nombre} {self.apellido}"

    def get_short_name(self):
        return self.nombre

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.admin

    @property
    def is_admin(self):
        return self.admin

    objects = UserManager()

    def __str__(self):
        return self.usuario

class Reserva(models.Model):
    cliente = models.CharField(max_length=30)
    fono = models.CharField(max_length=20)
    fecha = models.DateTimeField()
    estilista = models.CharField(max_length=30)
    estado = models.CharField(max_length=15)
    observacion = models.CharField(max_length=100)

class Producto(models.Model):
    producto = models.CharField(max_length=30)
    codigo = models.CharField(max_length=20)
    fechavencimiento = models.DateTimeField()
    marca = models.CharField(max_length=30)
    estado = models.CharField(max_length=15)
    observacion = models.CharField(max_length=100)    

class Estilista(models.Model):
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    disponible = models.BooleanField(default=True)