from calendar import c
from django.shortcuts import redirect
from django.shortcuts import render
from app.models import LOGIN, DETAILS, CUSTOMER_DETAILS, idgenerator, RATES, SHOP_DETAILS, TYPE_OF_WORK, WORKER_DETAILS, CONTRACTOR_DETAILS, COMPANY_DETAILS
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
import myapp.settings
from django.core.mail import send_mail
import math, random
from django.contrib import messages


# Create your views here.
def admin(request):
    return render(request,'admin_header.html')
def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def signup_company(request):
    data=idgenerator.objects.get(id=1)
    coid=data.coid
    com1=coid+1
    request.session['coid']=com1
    global com2
    com2="COM00"+str(com1)
    return render(request,'signup_company.html')
def signup_contractor(request):
    data=idgenerator.objects.get(id=1)
    cid=data.cid
    co1=cid+1
    request.session['cid']=co1
    global co2
    co2="CON00"+str(co1)
    d=TYPE_OF_WORK.objects.all()
    return render(request,'signup_contractor.html',{'d':d})
def signup_worker(request):
    data=idgenerator.objects.get(id=1)
    wid=data.wid
    w1=wid+1
    request.session['wid']=w1
    global w2
    w2="W00"+str(w1)
    d=TYPE_OF_WORK.objects.all()
    return render(request,'signup_worker.html',{'d':d})
def application(request):
    return render(request,'application.html')
def signup_customer(request):
    data=idgenerator.objects.get(id=1)
    cuid=data.cuid
    c1=cuid+1
    request.session['cuid']=c1
    global c2
    c2="CU00"+str(c1)
    return render(request,'signup_customer.html')
    
def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def customer_registration(request):
    c1=request.session['cuid']
    cus=CUSTOMER_DETAILS.objects.all()
    id="CU00"+str(c1)
    uname=request.POST.get('username')
    for i in cus:
        if i.cu_name == uname:
            messages.success(request, 'Username Already Exists')
            return redirect('/signup_customer/')
    data=idgenerator.objects.get(id=1)
    data.cuid=c1
    data.save()
    cud=DETAILS()
    cu=CUSTOMER_DETAILS()
    cud.D_id=id
    cud.Name=request.POST.get('Name')
    cud.Address=request.POST.get('Address')
    cud.Ph_no=request.POST.get('phno')
    cud.Email=request.POST.get('email')
    email=request.POST['email']
    cud.save()
    cu.Customer_id=id
    cu.status="not verified"
    cu.password=request.POST.get('password')
    cu.cu_name=request.POST.get('username')
    cu.save()
    global o
    o=generateOTP()
    subject = 'OTP Verification'
    message = f'Welcome to justclick Portal.\n Your OTP is: {o}'
    email_from = myapp.settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'verify_email.html',{'id':id})

def approve_cus(request):
    otp=request.POST.get('otp')
    id=request.POST.get('id')
    if otp == o:
        data=CUSTOMER_DETAILS.objects.get(Customer_id=id)
        data.status="verified"
        data.save()
        dat=LOGIN()
        dat.username=data.cu_name
        dat.password=data.password
        dat.type="customer"
        dat.save()
        return render(request,"login.html")
    else:
        messages.success(request, 'OTP is Incorrect')
        return render(request,'verify_email.html',{'id':id})

def worker_registration(request):
    w1=request.session['wid']
    w=WORKER_DETAILS.objects.all()
    id="W00"+str(w1)
    Uname=request.POST['username']
    for i in w:
        if i.U_name == Uname:
            messages.success(request, 'Username Already Exists')
            return redirect('/signup_worker/') 
    data=idgenerator.objects.get(id=1)
    data.wid=w1
    data.save()
    cud=DETAILS()
    cu=WORKER_DETAILS()
    cud.D_id=id
    cud.Name=request.POST.get('Name')
    cud.Address=request.POST.get('Address')
    cud.Ph_no=request.POST.get('phno')
    cud.Email=request.POST.get('email')
    cud.save()
    cu.Worker_id=id
    cu.status="not verified"
    cu.password=request.POST.get('password')
    cu.U_name=request.POST.get('username')
    cu.exp=request.POST.get('exp')
    cu.months=request.POST.get('expm')
    cu.city=request.POST.get('city')
    cu.pincode=request.POST.get('pincode')
    cu.Fd_of_work=request.POST.get('fd_of_work')
    cu.save()
    return render(request,'login.html')

def contractor_registration(request):
    co1=request.session['cid']
    con=CONTRACTOR_DETAILS.objects.all()
    id="CON00"+str(co1)
    Uname=request.POST['username']
    for i in con:
        if i.c_name == Uname:
            messages.success(request, 'Username Already Exists')
            return redirect('/signup_contractor/') 
    data=idgenerator.objects.get(id=1)
    data.cid=co1
    data.save()
    cud=DETAILS()
    cu=CONTRACTOR_DETAILS()
    cud.D_id=id
    cud.Name=request.POST.get('Name')
    cud.Address=request.POST.get('Address')
    cud.Ph_no=request.POST.get('phno')
    email=request.POST.get('email')
    cud.Email=email
    cud.save()
    cu.Contractor_id=id
    cu.status="not verified"
    cu.password=request.POST.get('password')
    cu.c_name=request.POST.get('username')
    cu.exp=request.POST.get('exp')
    cu.months=request.POST.get('expm')
    cu.city=request.POST.get('city')
    cu.pincode=request.POST.get('pincode')
    cu.Field_of_work=request.POST.get('fd_of_work')
    cu.save()
    subject = 'Successfull'
    message = f'Welcome to justclick Portal.\n Your under verification'
    email_from = myapp.settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'login.html')

def company_registration(request):
    com1=request.session['coid']
    com=COMPANY_DETAILS.objects.all()
    id="COM00"+str(com1)
    Uname=request.POST.get('username')
    for i in com:
        if i.co_name == Uname:
            messages.success(request, 'Username Already Exists')
            return redirect('/signup_company/')
    data=idgenerator.objects.get(id=1)
    data.coid=com1
    data.save()
    cud=DETAILS()
    cu=COMPANY_DETAILS()
    cud.D_id=id
    cud.Name=request.POST.get('Name')
    cud.Address=request.POST.get('Address')
    cud.Ph_no=request.POST.get('phno')
    cud.Email=request.POST.get('email')
    email=request.POST['email']
    cud.save()
    cu.Company_id=id
    cu.status="not verified"
    cu.password=request.POST.get('password')
    cu.co_name=request.POST.get('username')
    cu.li_no=request.POST.get('lic_no')
    cu.save()
    global o
    o=generateOTP()
    subject = 'OTP Verification'
    message = f'Welcome to justclick Portal.\n Your OTP is: {o}'
    email_from = myapp.settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'verify_email_com.html',{'id':id})

def approve_com(request):
    otp=request.POST.get('otp')
    id=request.POST.get('id')
    if otp == o:
        data=COMPANY_DETAILS.objects.get(Company_id=id)
        data.status="verified"
        data.save()
        dat=LOGIN()
        dat.username=data.co_name
        dat.password=data.password
        dat.type="company"
        dat.save()
        return render(request,"login.html")
    else:
        messages.success(request, 'OTP is Incorrect')
        return render(request,'verify_email_com.html',{'id':id})

def login_user(request):
    data=LOGIN.objects.all()
    us=request.POST.get('username')
    ps=request.POST.get('password')
    request.session['uid']=us
    flag=0
    for da in data:
        if us == da.username and ps == da.password:  
            T=da.type
            flag=1
            if T == 'admin':
                if 'uid' not in request.session:
                    return HttpResponse("/login/")
                else:
                    e=CUSTOMER_DETAILS.objects.filter(status="verified")
                    co=COMPANY_DETAILS.objects.filter(status="verified")
                    con=CONTRACTOR_DETAILS.objects.filter(status="not verified")
                    wor=WORKER_DETAILS.objects.filter(status="not verified")
                    d=TYPE_OF_WORK.objects.all()
                    return render(request,"admin_h.html",{"cus":e,"c":con,"w":wor,"com":co,"d":d})
            elif T == 'customer':
                return render(request,'customer_h.html')
            elif T == 'company':
                return render(request,'company_h.html')
            elif T == 'worker':
                return render(request,'worker_h.html')
            elif T == 'contractor':
                return render(request,'contractor_h.html')
    if flag == 0:
        messages.success(request, 'Incorrect Username or Password')
        return redirect('/login/')

def reg_user(request):
    if 'uid' not in request.session:
        return HttpResponse("invalid")
    else:
        e=CUSTOMER_DETAILS.objects.filter(status="verified")
        return render(request,"reg_user.html",{"w":e})

def reg_con(request):
    if 'uid' not in request.session:
        return HttpResponse("invalid")
    else:
        e=CONTRACTOR_DETAILS.objects.filter(status="not verified")
        return render(request,"reg_con.html",{'w':e})

def reg_wor(request):
    if 'uid' not in request.session:
        return HttpResponse("invalid")
    else:
        e=WORKER_DETAILS.objects.filter(status="not verified")
        return render(request,"reg_wor.html",{'w':e})

def reg_com(request):
    if 'uid' not in request.session:
        return HttpResponse("invalid")
    else:
        e=COMPANY_DETAILS.objects.filter(status="verified")
        return render(request,"reg_com.html",{'w':e})

def edit_cus(request,Customer_id):
    if 'uid' not in request.session:
        return HttpResponse("invalid")
    else:
        data=DETAILS.objects.get(D_id=Customer_id)
        return render(request,'edit_cus.html',{'dd':data})

def edit_con(request,Contractor_id):
    if 'uid' not in request.session:
        return HttpResponse("invalid")
    else:
        data=DETAILS.objects.get(D_id=Contractor_id)
        return render(request,'edit_con.html',{'dd':data})

def edit_wor(request,Worker_id):
    if 'uid' not in request.session:
        return HttpResponse("invalid")
    else:
        data=DETAILS.objects.get(D_id=Worker_id)
        return render(request,'edit_wor.html',{'dd':data})

def edit_com(request,Company_id):
    if 'uid' not in request.session:
        return HttpResponse("invalid")
    else:
        data=DETAILS.objects.get(D_id=Company_id)
        return render(request,'edit_com.html',{'dd':data})

def reject_cus(request,D_id):
    d=CUSTOMER_DETAILS.objects.get(Customer_id=D_id)
    d.status="rejected"
    d.save()
    return render(request,"admin_h.html")

def approve_con(request,D_id):
    data=CONTRACTOR_DETAILS.objects.get(Contractor_id=D_id)
    d=DETAILS.objects.get(D_id=D_id)
    email=d.Email
    data.status="verified"
    data.save()
    dat=LOGIN()
    dat.username=data.c_name
    dat.password=data.password
    dat.type="contractor"
    dat.save()
    subject = 'Verification'
    message = f'Your Verification is completed\n Please Login With Your Credentials'
    email_from = myapp.settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,"admin_h.html")

def reject_con(request,D_id):
    d=CONTRACTOR_DETAILS.objects.get(Contractor_id=D_id)
    det=DETAILS.objects.get(D_id=D_id)
    email=det.Email
    d.status="rejected"
    d.save()
    subject = 'Verification'
    message = f'Unfortunately justclick Was Unable to Verify, That Your a Contractor'
    email_from = myapp.settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,"admin_h.html")

def approve_wor(request,D_id):
    data=WORKER_DETAILS.objects.get(Worker_id=D_id)
    d=DETAILS.objects.get(D_id=D_id)
    email=d.Email
    data.status="verified"
    data.save()
    dat=LOGIN()
    dat.username=data.U_name
    dat.password=data.password
    dat.type="worker"
    dat.save()
    subject = 'Verification'
    message = f'Your Verification is completed\n Please Login With Your Credentials'
    email_from = myapp.settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,"admin_h.html")

def reject_wor(request,D_id):
    d=WORKER_DETAILS.objects.get(Worker_id=D_id)
    det=DETAILS.objects.get(D_id=D_id)
    email=det.Email
    d.status="rejected"
    d.save()
    subject = 'Verification'
    message = f'Unfortunately justclick Was Unable to Verify, That Your a Worker'
    email_from = myapp.settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,"admin_h.html")

def reject_com(request,D_id):
    d=COMPANY_DETAILS.objects.get(Company_id=D_id)
    d.status="rejected"
    d.save()
    return render(request,"admin_h.html")
def logout(request):
    if 'uid' not in request.session:
        return HttpResponse("You Have Already Loged Out")
    else:
        request.session['uid']=""
        del request.session['uid']
        return redirect('/index/')

def verify_email(request):
    return render(request,'verify_email.html')
def email_form(request):
    return render(request,'email_form.html')
def add_shop(request):
    if 'uid' not in request.session:
        return HttpResponse("/login/")
    else:
        data=idgenerator.objects.get(id=1)
        sid=data.sid
        s1=sid+1
        s2="S00"+str(s1)
        data.sid=s1
        data.save()
        d=SHOP_DETAILS()
        d.Shop_id=s2
        d.Type_id=request.POST.get('field_of_work')
        d.Shop_name=request.POST.get('shop_name')
        d.Address=request.POST.get('address')
        d.City=request.POST.get('city')
        d.pincode=request.POST.get('pincode')
        d.Ph_no=request.POST.get('phno')
        d.save()
        return HttpResponse("Shop added Successfully")
def add_rates(request):
    if 'uid' not in request.session:
        return redirect("/login/")
    else:
        data=idgenerator.objects.get(id=1)
        rid=data.rid
        r1=rid+1
        r2="R00"+str(r1)
        data.rid=r1
        data.save()
        d=RATES()
        d.Rate_id=r2
        d.Type_id=request.POST.get('field_of_work')
        d.Rate_type=request.POST.get('rate_type')
        d.Rate=request.POST.get('rate')
        d.M_name=request.POST.get('m_name')
        d.M_Rate=request.POST.get('m_rate')
        d.save()
        return HttpResponse("Rates added Successfully")

def show_shops(request):
    if 'uid' not in request.session:
        return redirect("/login/")
    else:
        data=SHOP_DETAILS.objects.all()
        dat=TYPE_OF_WORK.objects.all()
        return render(request,"show_shops.html",{"d":data,"c":dat})
def show_rates(request):
    if 'uid' not in request.session:
        return redirect("/login/")
    else:
        data=RATES.objects.all()
        dat=TYPE_OF_WORK.objects.all()
        return render(request,"show_rates.html",{"d":data,"c":dat})

        
        
