from django.db import models
from django.contrib.auth.models import User

class Type(models.Model) :
    name = models.CharField(max_length=255 , unique=True)
    
    def __str__(self) :
        return self.name

class Adhkar(models.Model) :
    text = models.TextField()
    type = models.ForeignKey(Type, on_delete=models.PROTECT , related_name="adkar")

    def __str__(self) :
        return f"{self.text} : {self.type.name}"

class DoaaType(models.Model) :
    name = models.CharField(max_length=255 , unique=True)
    
    def __str__(self) :
        return self.name

class Doaa(models.Model) :
    text = models.CharField(max_length=255)
    type = models.ForeignKey(DoaaType, on_delete=models.CASCADE, related_name="doaa")

class Tasbih(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tasbih')
    tasbih_count = models.PositiveIntegerField(default = 0)