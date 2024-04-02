from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True, primary_key=True)
    password = models.CharField(max_length=128)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.username


class Recipe(models.Model):
    DIFFICULTY_LEVELS = (
        ('Jednoduchá', 'Jednoduchá'),
        ('Střední', 'Střední'),
        ('Težká', 'Težká'),
    )
    name = models.CharField(max_length=120)
    ingredients = models.CharField(max_length=400)
    picture = models.FileField()
    difficulty = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10)
    prep_time = models.PositiveIntegerField()
    prep_guide = models.TextField()
    tags = models.ManyToManyField(Tag)
    users_favorited = models.ManyToManyField(CustomUser, related_name='favorited_recipes')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=CustomUser.objects.get(username="uziv").username)

    def __str__(self):
        return "Recipe for {}".format(self.name)







