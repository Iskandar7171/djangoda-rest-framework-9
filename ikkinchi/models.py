from django.db import models
class Salom1(models.Model):
    name = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="birinchi/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Salom2(models.Model):
    name = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="birinchi/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Salom3(models.Model):
    name = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="birinchi/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Salom4(models.Model):
    name = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="birinchi/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Salom5(models.Model):
    name = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="birinchi/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

