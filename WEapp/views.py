from django.shortcuts import render,redirect
from MYapp.models import catdb,productdb
from WEapp.models import customerdb

# Create your views here.
def webpage(request):
    details = catdb.objects.all()
    return render(request,"homepage.html",{'details':details})
def aboutus(request):
    data = catdb.objects.all()
    return render(request, "about.html",{'data':data})
def contactus(request):
    data = catdb.objects.all()
    return render(request, "contactus.html",{'data':data})

def discategory(request,itemCatg):
    data = catdb.objects.all()
    print("===itemCatg===",itemCatg)
    catg=itemCatg.upper()
    products = productdb.objects.filter(category=itemCatg)
    context={
        'products':products,
        'catg':catg,
        'data':data
    }

    return render(request,"displaycategory.html",context)

def products(request):
    products=productdb.objects.all()
    data = catdb.objects.all()
    return render(request,"product.html",{'products':products,'data':data})
def productdetails(request,dataid):
    datas=productdb.objects.get(id=dataid)
    data = catdb.objects.all()
    return render(request, "productdetails.html",{'dat':datas,'data':data})

def weblogin(request):
    data = catdb.objects.all()
    return render(request, "websitelogin.html", {'data': data})

def regdata(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('pass1')
        confirmpassword=request.POST.get('pass2')
        if password==confirmpassword:
            obj=customerdb(username=username,email=email,password=password,confirmpassword=confirmpassword)
            obj.save()
            return redirect(weblogin)
        else:
            return render(request,'websitelogin.html',{'msg':"sorry password not matched"})


def customerlogin(request):
    if request.method=='POST':
        username_r=request.POST.get("username")
        password_r=request.POST.get("password")
        if customerdb.objects.filter(username=username_r,password=password_r).exists():
            request.session['username']=username_r
            request.session['password']=password_r


            return redirect(webpage)
        else:
            return render(request,'websitelogin.html',{'msg':"sorry...invalid paasword or username"})
def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(webpage)