from django.contrib.auth import password_validation, authenticate
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator, FileExtensionValidator
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from .models import User

# Modelo para mostrar los campo al usuario
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )

# Login de usuarios
class UserLoginSerializer(serializers.Serializer):
    # Campos que se ocupan para el login
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=40)

    # Validacion de datos
    def validate(self, data):
        # authenticate recibe las credenciales para validarlos
        user = authenticate(email=data["email"], password=data["password"])
        
        if user is None:
            raise serializers.ValidationError("Las credenciales no son validas")

        # Guardamos el usuario en el contexto
        self.context["user"] = user
        return data

    # Crea un nuevo usuario junto con el token
    def create(self, data):
        # Generar o recuperar Token
        token, created = Token.objects.get_or_create(user=self.context["user"])
        return self.context["user"], token.key

# Registro de usuarios
class UserSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    photo = serializers.ImageField(
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg"])],
        required=False,
    )

    description = serializers.CharField(max_length=300, required=False)
    city = serializers.CharField(max_length=80, required=False)
    country = serializers.CharField(max_length=80, required=False)
    phone_regex = RegexValidator(
        regex=r"\+?1?\d{9,15}$",
        message="Debes introducir un numero correcto con el formato (+999999999). El limite son 15 digitos",
    )
    phone = serializers.CharField(validators=[phone_regex], required=False)
    password = serializers.CharField(min_length=8, max_length=50)
    password_confirmation = serializers.CharField(min_length=8, max_length=50)
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    # Validacion de campos
    def validate(self, data):
        passwd = data["password"]
        passwd_conf = data["password_confirmation"]

        # Valida si las contraseñas son iguales
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(passwd)

        # Valida si en el formulario exite el campo photo
        image = None
        if "photo" in data:
            image = data["photo"]

        # Comprueba el tamaño de la imagen. Que no exceda a 512KB
        if image:
            if image.size > (512 * 1024):
                raise serializers.ValidationError(
                    f"La imagen es demasiado grande, el peso máximo permitido es de 512KB y el tamaño enviado es de {round(image.size / 1024)}KB"
                )
        
        return data

    # Creacion del usuario despues de las validaciones
    def create(self, data):
        data.pop("password_confirmation")

        # Encripta el password
        data["password"]=make_password(data["password"])
        user = User.objects.create(**data)
        return user

class UserLogoutSerializer(serializers.Serializer):
    # Generar o recuperar Token
    def get_attribute(self, instance):
        token = Token.objects.get_or_create(user=self.context["user"])
        return token
