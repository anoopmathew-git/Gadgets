from django.db import models
class admindb(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    mob=models.IntegerField(null=True,blank=True)
    image=models.ImageField(upload_to="profile",null=True,blank=True)
    username=models.CharField(max_length=50,null=True,blank=True)
    pswd=models.CharField(max_length=50,null=True,blank=True)
    cpswd=models.CharField(max_length=50, null=True, blank=True)
class catdb(models.Model):
    catname=models.CharField(max_length=50,null=True,blank=True)
    image=models.ImageField(upload_to="profile",null=True,blank=True)
    cdes=models.CharField(max_length=100,null=True,blank=True)

class productdb(models.Model):
    category=models.CharField(max_length=50,null=True,blank=True)
    pname=models.CharField(max_length=50,null=True,blank=True)
    pquantity=models.IntegerField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    image=models.ImageField(upload_to="profile",null=True,blank=True)
