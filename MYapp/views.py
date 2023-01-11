from django.shortcuts import render,redirect
from MYapp.models import admindb,catdb,productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

def mainpage(request):
    return render(request,"index.html")
def addadminpage(request):
    return render(request,"addadmin.html")
def adminsave(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        mb=request.POST.get('mobile')
        usr=request.POST.get('username')
        pw=request.POST.get('pswd')
        cpw=request.POST.get('cpswd')
        im=request.FILES['img']
        object=admindb(name=na,email=em,mob=mb,username=usr,pswd=pw,cpswd=cpw, image=im)
        object.save()
        return redirect(addadminpage)
def disadminpage(request):
    data=admindb.objects.all()
    return render(request,"displayadmin.html",{'data':data})
def editpage(request,dataid):
    data=admindb.objects.get(id=dataid)
    print(data)
    return render(request,"editdata.html",{'data':data})
def updatedata(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        mb = request.POST.get('mobile')
        usr = request.POST.get('username')
        pw = request.POST.get('pswd')
        cpw = request.POST.get('cpswd')
        try:
            im=request.FILES['img']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=admindb.objects.get(id=dataid).image
        admindb.objects.filter(id=dataid).update(name=na,email=em,mob=mb,username=usr,pswd=pw,cpswd=cpw, image=file)
        return redirect(disadminpage)

def deleteadmin(req, dataid):
    data = admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(disadminpage)
def addcatpage(request):
    return render(request,"addcat.html")
def addcatsave(request):
    if request.method=="POST":
        cna=request.POST.get('cname')
        cdes=request.POST.get('description')
        img=request.FILES['image']
        obj=catdb(catname=cna,cdes=cdes,image=img)
        obj.save()
        return redirect(addcatpage)

def catdisplaypage(request):
    data =catdb.objects.all()
    return render(request,"catdisplay.html",{'data': data})
def cateditpage(request,dataid):
    data=catdb.objects.get(id=dataid)
    print(data)
    return render(request,"catedit.html",{'data':data})
def catupdate(request,dataid):
    if request.method=="POST":
        cna = request.POST.get('cname')
        cdes = request.POST.get('description')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=catdb.objects.get(id=dataid).image
        catdb.objects.filter(id=dataid).update(catname=cna,cdes=cdes,image=file)
        return redirect(catdisplaypage)



def deletecat(req, dataid):
    data=catdb.objects.filter(id=dataid)
    data.delete()
    return redirect(catdisplaypage)
def productpage(request):
    data=catdb.objects.all()
    return render(request,"addproduct.html",{"data":data})
def productsave(request):
    if request.method == "POST":
        cpna=request.POST.get('cname')
        pname=request.POST.get('pname')
        pqnty=request.POST.get('pqnty')
        price= request.POST.get('price')
        img = request.FILES['image']
        obj=productdb(category=cpna,pname=pname,pquantity=pqnty,price=price,image=img)
        obj.save()
        return redirect(productpage)
def productdisplaypage(request):
    data=productdb.objects.all()
    return render(request,"productdisplay.html",{'data': data})
def producteditpage(request,dataid):
    data=productdb.objects.get(id=dataid)
    da=catdb.objects.all()
    return render(request,"productedit.html",{'data':data,'da':da})
def productupdate(request,dataid):
    if request.method=="POST":
        cpna = request.POST.get('cname')
        pname = request.POST.get('pname')
        pqnty = request.POST.get('pqnty')
        price = request.POST.get('price')

        try:
            im=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=dataid).image
        productdb.objects.filter(id=dataid).update(category=cpna,pname=pname,pquantity=pqnty,price=price, image=file)
        return redirect(productdisplaypage)

def deleteproduct(req, dataid):
    data=productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(productdisplaypage)
def loginpage(request):
    return render(request,"login.html")
def adminlogin(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(mainpage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)