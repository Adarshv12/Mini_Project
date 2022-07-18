from calendar import c
from email.headerregistry import Address
from xml.sax.handler import DTDHandler
from django.shortcuts import redirect
from django.shortcuts import render
from app.models import LOGIN, DETAILS, CUSTOMER_DETAILS, idgenerator, RATES, SHOP_DETAILS, \
TYPE_OF_WORK, WORKER_DETAILS, CONTRACTOR_DETAILS, Photos, Messages,work_invite,suggestions, tbl_projects, tbl_contractor_invite,\
tbl_quotation, tbl_payment_request,tbl_payments,tbl_progress,tbl_rating
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
import myapp.settings
from django.core.mail import send_mail
import math, random
from django.contrib import messages 
from django.core import serializers  
from django.views import View
import json
from django.views.decorators.cache import cache_control
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


# Create your views here.


def test(request):
    currency = 'INR'
    amount = 20000  # Rs. 200
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    return render(request,'test.html',context=context)
def admin(request):
    return render(request,'admin_header.html')


def index(request):
    r=Photos.objects.all()
    dc=Photos.objects.filter(userid__istartswith='CON').order_by('-date')[:3]
    d=Photos.objects.filter(userid__istartswith='W').order_by('-date')[:5]
    det=DETAILS.objects.all()
    return render(request,'index.html',{"data":d,"det":det,"r":r,'dc':dc})
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
    email=request.POST.get('email')
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
    subject = 'Successfull'
    message = f'Welcome to justclick Portal.\n You are under verification'
    email_from = myapp.settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
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
    message = f'Welcome to justclick Portal.\n You are under verification'
    email_from = myapp.settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('/login/')

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

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_user(request):
    data=LOGIN.objects.all()
    us=request.POST.get('username')
    ps=request.POST.get('password')
    flag=0
    for da in data:
        if us == da.username and ps == da.password:  
            T=da.type
            flag=1
            if T == 'admin':
                request.session['uid']=us
                return redirect('/login_admin/')
            elif T == 'customer':
                request.session['cusid']=us
                return redirect('/login_cus/')
            elif T == 'company':
                request.session['uid']=us
                return render(request,'company_h.html')
            elif T == 'worker':
                request.session['woid']=us
                return redirect('/login_worker/')
            elif T == 'contractor':
                request.session['conid']=us
                return redirect('/login_con/')
    if flag == 0:
        messages.success(request, 'Incorrect Username or Password')
        return redirect('/login/')

# Customer modules -----------------------------------------------------------------------------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_con(request):
    if 'conid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        usid=request.session['conid']
        
        d=CONTRACTOR_DETAILS.objects.get(c_name=usid)
        con_id=d.Contractor_id
        p=tbl_contractor_invite.objects.filter(status='1') & tbl_contractor_invite.objects.filter(Contractor_id=con_id)
        list = []
        for a in p:
            pd=tbl_projects.objects.get(id=a.Project_id)
            list.append(pd)
        pr=tbl_contractor_invite.objects.filter(Contractor_id=con_id) & (tbl_contractor_invite.objects.filter(status='0'))
        c=pr.count()
        dat=Photos.objects.filter(userid=con_id).order_by('-id')[:5]
        return render(request,'contractor_h.html',{'data':d,'c':c,'p':dat,'l':list})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_worker(request):
    if 'woid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        usid=request.session['woid']
        d=WORKER_DETAILS.objects.get(U_name=usid)
        wor_id=d.Worker_id
        w=work_invite.objects.filter(Worker_id=wor_id) & work_invite.objects.filter(Status='0')
        all=work_invite.objects.filter(Worker_id=wor_id)
        c=w.count()
        details=DETAILS.objects.get(D_id=wor_id)
        dat=Photos.objects.filter(userid=wor_id).order_by('-id')[:5]
        return render(request,"worker_h.html",{"data":d,"p":dat,"w":details,'wi':all,'c':c})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_cus(request):
    if 'cusid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        usid=request.session['cusid']
        d=CUSTOMER_DETAILS.objects.get(cu_name=usid)
        cus_id=d.Customer_id
        q=tbl_quotation.objects.filter(Customer_id=cus_id) & (tbl_quotation.objects.filter(status='0'))
        p=tbl_projects.objects.filter(Customer_id=cus_id)
        c=q.count()
        details=DETAILS.objects.get(D_id=cus_id)
        t=TYPE_OF_WORK.objects.all()
        return render(request,'customer_h.html',{'data':details,'d':d,'t':t,'c':c,'q':q,'p':p})

def user_edit(request,Customer_id):
    if 'cusid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        d=DETAILS.objects.get(D_id=Customer_id)
        f=CUSTOMER_DETAILS.objects.get(Customer_id=Customer_id)
        return render(request,"user_edit.html",{'d':d,'f':f})

def update_user(request):
    unm=request.POST.get('uname')
    d=CUSTOMER_DETAILS.objects.get(cu_name=unm)
    id=d.Customer_id
    data=DETAILS.objects.get(D_id=id)
    data.Address=request.POST.get('address')
    data.Ph_no=request.POST.get('phno')
    em=request.POST.get('email')
    data.Email=em
    data.save()
    subject = 'Profile Update'
    message = f'Details Updated Succesfully'
    email_from = myapp.settings.EMAIL_HOST_USER
    recipient_list = [em]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('/login_cus/')

@cache_control(no_cache=True, must_revalidate=True)
def logout_cus(request):
    if 'cusid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        request.session['cusid']=""
        del request.session['cusid']
        return redirect('/index/')

@cache_control(no_cache=True, must_revalidate=True)
def logout_con(request):
    if 'conid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        request.session['conid']=""
        del request.session['conid']
        return redirect('/index/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_admin(request):
    if 'uid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        wcount=WORKER_DETAILS.objects.filter(status="not verified")
        ccount=CONTRACTOR_DETAILS.objects.filter(status="not verified")
        e=CUSTOMER_DETAILS.objects.filter(status="verified") | CUSTOMER_DETAILS.objects.filter(status="rejected")
        co=COMPANY_DETAILS.objects.filter(status="verified") | COMPANY_DETAILS.objects.filter(status="rejected")
        con=CONTRACTOR_DETAILS.objects.filter(status="not verified") | CONTRACTOR_DETAILS.objects.filter(status="verified") | CONTRACTOR_DETAILS.objects.filter(status="rejected")
        wor=WORKER_DETAILS.objects.filter(status="not verified") | WORKER_DETAILS.objects.filter(status="verified") | WORKER_DETAILS.objects.filter(status="rejected")
        cou_user=wcount.count()+ccount.count()
        d=TYPE_OF_WORK.objects.all()
        m=Messages.objects.all().order_by('-id')[:3]
        count=m.count()
        return render(request,"admin_h.html",{"cus":e,"c":con,"w":wor,"com":co,"d":d,"m":m,"count":count,"cou_user":cou_user})


def edit_cus(request,Customer_id):
    if 'uid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        data=DETAILS.objects.get(D_id=Customer_id)
        return render(request,'edit_cus.html',{'dd':data})

def edit_con(request,Contractor_id,status):
    if 'uid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        if status == 'not verified':
            data=DETAILS.objects.get(D_id=Contractor_id)
            return render(request,'edit_con.html',{'dd':data})
        else:
            data=DETAILS.objects.get(D_id=Contractor_id)
            return render(request,'edit1_con.html',{'dd':data})

def edit_wor(request,Worker_id,status):
    if 'uid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        if status == 'not verified':
            data=DETAILS.objects.get(D_id=Worker_id)
            return render(request,'edit_wor.html',{'dd':data})
        else:
            data=DETAILS.objects.get(D_id=Worker_id)
            return render(request,'edit1_wor.html',{'dd':data})

def edit_com(request,Company_id):
    if 'uid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        data=DETAILS.objects.get(D_id=Company_id)
        return render(request,'edit_com.html',{'dd':data})

def reject_cus(request,D_id):
    d=CUSTOMER_DETAILS.objects.get(Customer_id=D_id)
    id=d.cu_name
    d.status="rejected"
    d.save()
    dat=LOGIN.objects.get(username=id)
    dat.delete()
    return redirect('/login_admin/')

def reject_com(request,D_id):
    d=COMPANY_DETAILS.objects.get(Company_id=D_id)
    id=d.co_name
    d.status="rejected"
    d.save()
    dat=LOGIN.objects.get(username=id)
    dat.delete()
    return redirect('/login_admin/')


def approve1_cus(request,D_id):
    data=CUSTOMER_DETAILS.objects.get(Customer_id=D_id)
    data.status="verified"
    data.save()
    dat=LOGIN()
    dat.username=data.cu_name
    dat.password=data.password
    dat.type='customer'
    dat.save()
    return redirect('/login_admin/')

def approve1_com(request,D_id):
    data=COMPANY_DETAILS.objects.get(Company_id=D_id)
    data.status="verified"
    data.save()
    dat=LOGIN()
    dat.username=data.co_name
    dat.password=data.password
    dat.type='company'
    dat.save()
    return redirect('/login_admin/')
    
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
    return redirect('/login_admin/')

def approve1_con(request,D_id):
    data=CONTRACTOR_DETAILS.objects.get(Contractor_id=D_id)
    d=DETAILS.objects.get(D_id=D_id)
    data.status="verified"
    data.save()
    dat=LOGIN()
    dat.username=data.c_name
    dat.password=data.password
    dat.type="contractor"
    dat.save()
    # subject = 'Verification'
    # message = f'Your Verification is completed\n Please Login With Your Credentials'
    # email_from = myapp.settings.EMAIL_HOST_USER
    # recipient_list = [email]
    # send_mail( subject, message, email_from, recipient_list )
    return redirect('/login_admin/')

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
    return redirect("/login_admin/")

def reject1_con(request,D_id):
    d=CONTRACTOR_DETAILS.objects.get(Contractor_id=D_id)
    id=d.c_name
    d.status="rejected"
    d.save()
    dat=LOGIN.objects.get(username=id)
    dat.delete()
    # subject = 'Verification'
    # message = f'Unfortunately justclick Was Unable to Verify, That Your a Contractor'
    # email_from = myapp.settings.EMAIL_HOST_USER
    # recipient_list = [email]
    # send_mail( subject, message, email_from, recipient_list )
    return redirect("/login_admin/")

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
    return redirect('/login_admin/')

def approve1_wor(request,D_id):
    data=WORKER_DETAILS.objects.get(Worker_id=D_id)
    d=DETAILS.objects.get(D_id=D_id)
    data.status="verified"
    data.save()
    dat=LOGIN()
    dat.username=data.U_name
    dat.password=data.password
    dat.type="worker"
    dat.save()
    # subject = 'Verification'
    # message = f'Your Verification is completed\n Please Login With Your Credentials'
    # email_from = myapp.settings.EMAIL_HOST_USER
    # recipient_list = [email]
    # send_mail( subject, message, email_from, recipient_list )
    return redirect('/login_admin/')

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
    return redirect('/login_admin/')

def reject1_wor(request,D_id):
    d=WORKER_DETAILS.objects.get(Worker_id=D_id)
    id=d.U_name
    d.status="rejected"
    d.save()
    dat=LOGIN.objects.get(username=id)
    dat.delete()
    # subject = 'Verification'
    # message = f'Unfortunately justclick Was Unable to Verify, That Your a Worker'
    # email_from = myapp.settings.EMAIL_HOST_USER
    # recipient_list = [email]
    # send_mail( subject, message, email_from, recipient_list )
    return redirect('/login_admin/')


# logout views ````````````````````````````````````````````````````````````````````````````````````````````
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    if 'uid' not in request.session:
        messages.success(request, 'Session Expired Login Again')
        return redirect('/login/')
    else:
        request.session['uid']=""
        del request.session['uid']
        return redirect('/index/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_worker(request):
    if 'woid' not in request.session:
        messages.success(request, 'Session Expired Login Again')
        return redirect('/login/')
    else:
        request.session['woid']=""
        del request.session['woid']
        return redirect('/index/')

def verify_email(request):
    return render(request,'verify_email.html')
def email_form(request):
    return render(request,'email_form.html')

def add_shop(request):
    if 'uid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
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
        messages.success(request, 'Shop Added Successfully')
        return redirect('/login_admin/')
def add_rates(request):
    if 'uid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
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
        d.save()
        messages.success(request, 'Rates Added Successfully')
        return redirect('/login_admin/')

def show_shops(request):
    if 'uid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        data=SHOP_DETAILS.objects.all()
        dat=TYPE_OF_WORK.objects.all()
        return render(request,"show_shops.html",{"d":data,"c":dat})
def show_rates(request):
    if 'uid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        data=RATES.objects.all()
        dat=TYPE_OF_WORK.objects.all()
        return render(request,"show_rates.html",{"d":data,"c":dat})

def edit_rate(request):
    id=request.POST.get('rateid')
    r=RATES.objects.get(Rate_id=id)
    r.Rate=request.POST.get('rate')
    r.save()
    return redirect("/show_rates/")

def del_rate(request,Rate_id):
    r=RATES.objects.get(Rate_id=Rate_id)
    r.delete()
    return redirect("/show_rates/")

def del_shop(request,Shop_id):
    s=SHOP_DETAILS.objects.get(Shop_id=Shop_id)
    s.delete()
    return redirect("/show_shops/")

# worker modules

def add_image(request):
    if 'woid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        d=Photos()
        d.userid=request.POST.get('userid')
        d.Title=request.POST.get('title')
        d.user_name=request.POST.get('uname')
        Photo=request.FILES['photo']
        fs=FileSystemStorage()
        fn=fs.save(Photo.name,Photo)
        uploaded_file_url=fs.url(fn)
        d.image=uploaded_file_url
        d.save()
        messages.success(request, 'Image added Successfully')
        return redirect('/login_worker/')
def show_image(request,Worker_id):
    if 'woid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        d=Photos.objects.filter(userid=Worker_id)
        return render(request,"show_image.html",{"data":d})

def worker_edit(request,Worker_id):
    if 'woid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        d=DETAILS.objects.get(D_id=Worker_id)
        f=WORKER_DETAILS.objects.get(Worker_id=Worker_id)
        return render(request,"worker_edit.html",{'d':d,'f':f})

def update_worker(request):
    unm=request.POST.get('uname')
    d=WORKER_DETAILS.objects.get(U_name=unm)
    id=d.Worker_id
    data=DETAILS.objects.get(D_id=id)
    data.Address=request.POST.get('address')
    d.city=request.POST.get('city')
    fs=FileSystemStorage()
    Photo=request.FILES['pimage']
    fn=fs.save(Photo.name,Photo)
    uploaded_file_url=fs.url(fn)
    d.profile_image=uploaded_file_url
    data.Ph_no=request.POST.get('phno')
    em=request.POST.get('email')
    data.Email=em
    data.save()
    d.save()
    subject = 'Profile Update'
    message = f'Details Updated Succesfully'
    email_from = myapp.settings.EMAIL_HOST_USER
    recipient_list = [em]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('/login_worker/')

def message(request):
    m=Messages()
    m.Name=request.POST.get('name')
    m.Subject=request.POST.get('subject')
    m.Message=request.POST.get('message')
    email=request.POST.get('email')
    m.Email=email
    m.save()
    subject = 'Thank You'
    message = f'We Got Your Message.\n We will Contact you Shortly'
    email_from = myapp.settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
    return redirect("/index/")
def profile(request):
    if request.method == 'GET':
           u_id = request.GET['post_id']
           uname = WORKER_DETAILS.objects.get(U_name=u_id)
           data={'pr':uname}
           return HttpResponse('not working')        
    
    else:
           return HttpResponse("Request method is not a GET")
        
class dataview(View):

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            Det=DETAILS.objects.all()
            det_ser=serializers.serialize('json',Det)
            return JsonResponse(det_ser,safe=False)
        return JsonResponse({'message':'Wrong validation'})

def user_search(request):
    if 'cusid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        if request.method == 'POST':
            search_str=json.loads(request.body).get('searchtxt')
            type=json.loads(request.body).get('typeofwork')

            result=WORKER_DETAILS.objects.filter(Fd_of_work=type) & (WORKER_DETAILS.objects.filter(city__istartswith=search_str) | WORKER_DETAILS.objects.filter(pincode__istartswith=search_str))
            data=result.values()
            return JsonResponse(list(data), safe=False)

def type_search(request):
    if 'cusid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        if request.method == 'POST':
            search_str=json.loads(request.body).get('searchtxt')
            
            result=WORKER_DETAILS.objects.filter(Fd_of_work__istartswith=search_str) 
            data=result.values()
            return JsonResponse(list(data), safe=False)

def place_search(request):
    if 'cusid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        if request.method == 'POST':
            search_str=json.loads(request.body).get('searchtxt')

            result=WORKER_DETAILS.objects.filter(city__istartswith=search_str) 
            data=result.values()
            return JsonResponse(list(data), safe=False)

def pin_search(request):
    if 'cusid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        if request.method == 'POST':
            search_str=json.loads(request.body).get('searchtxt')

            result=WORKER_DETAILS.objects.filter(pincode__istartswith=search_str) 
            data=result.values()
            return JsonResponse(list(data), safe=False)

def view_user(request):
    if request.method == 'POST':
        name=json.loads(request.body).get('uname')

        w=WORKER_DETAILS.objects.get(U_name=name)
        id=w.Worker_id
        d=DETAILS.objects.filter(D_id=id)
        data=d.values()
        return JsonResponse(list(data), safe=False)
        


def view_search(request,D_id):
    if 'cusid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        c=request.session['cusid']
        f=WORKER_DETAILS.objects.filter(Worker_id=D_id)
        return render(request, 'invite_worker.html',{'t':f,'c':c})


    

def add_work_invite(request):
    w=work_invite()
    cusid=request.POST.get('cid')
    d=CUSTOMER_DETAILS.objects.get(cu_name=cusid)
    d_id=d.Customer_id
    dat=DETAILS.objects.get(D_id=d_id)
    email=dat.Email
    w.Type=request.POST.get('type')
    w.Desc=request.POST.get('desc')
    w.Loc=request.POST.get('loc')
    w.Worker_id=request.POST.get('wid')
    w.Customer_id=d_id
    w.Status="0"
    w.save()
    subject = 'Work Invite'
    message = f'Work Invite Successfully send'
    email_from = myapp.settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return redirect('/login_cus/')

def winvite_accept(request,id):
    if 'woid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        w=work_invite.objects.get(id=id)
        w.Status="1"
        did=w.Customer_id
        w.save()
        d=DETAILS.objects.get(D_id=did)
        name=d.Name
        email=d.Email
        subject = 'Work Invite'
        message = f'Your Work Invite is Accepted By'
        email_from = myapp.settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        return redirect('/login_worker/')

def winvite_reject(request,id):
    if 'woid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        w=work_invite.objects.get(id=id)
        w.Status="2"
        did=w.Customer_id
        w.save()
        d=DETAILS.objects.get(D_id=did)
        name=d.Name
        email=d.Email
        subject = 'Work Invite'
        message = f'Your Work Invite is Rejected By'
        email_from = myapp.settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        return redirect('/login_worker/')

def winvite_view(request,id):
    if 'woid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        w=work_invite.objects.get(id=id)
        did=w.Customer_id
        d=DETAILS.objects.get(D_id=did)
        return render(request,'winvite_view.html',{'d':d})

def worker_back(request):
    return redirect('/login_worker/')

def view_winvite(request,uname):
    if 'cusid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        w=CUSTOMER_DETAILS.objects.get(cu_name=uname)
        id=w.Customer_id
        d=work_invite.objects.filter(Customer_id=id)
        return render(request,'view_winvite.html',{'d':d})

def add_project(request):
    if 'cusid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        cusid=request.session['cusid']
        data=CUSTOMER_DETAILS.objects.get(cu_name=cusid)
        cid=data.Customer_id
        d=TYPE_OF_WORK.objects.all()
        city=CONTRACTOR_DETAILS.objects.all().values('city').distinct()
        return render(request,'add_project.html',{'d':d,'city':city,'cid':cid})

def contractor_edit(request,Contractor_id):
    if 'conid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        d=DETAILS.objects.get(D_id=Contractor_id)
        f=CONTRACTOR_DETAILS.objects.get(Contractor_id=Contractor_id)
        return render(request,"contractor_edit.html",{'d':d,'f':f})

def update_contractor(request):
    unm=request.POST.get('uname')
    d=CONTRACTOR_DETAILS.objects.get(c_name=unm)
    id=d.Contractor_id
    data=DETAILS.objects.get(D_id=id)
    data.Address=request.POST.get('address')
    d.city=request.POST.get('city')
    fs=FileSystemStorage()
    Photo=request.FILES['pimage']
    fn=fs.save(Photo.name,Photo)
    uploaded_file_url=fs.url(fn)
    d.profile_image=uploaded_file_url
    data.Ph_no=request.POST.get('phno')
    em=request.POST.get('email')
    data.Email=em
    data.save()
    d.save()
    subject = 'Profile Update'
    message = f'Details Updated Succesfully'
    email_from = myapp.settings.EMAIL_HOST_USER
    recipient_list = [em]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('/login_con/')

def type_select(request):
    if request.method == 'POST':
        search_str=json.loads(request.body).get('type')
            
        result=suggestions.objects.filter(Type=search_str) 
        data=result.values()
        return JsonResponse(list(data), safe=False)

def get_worker_id(request):
    if request.method == 'POST':
        search_str=json.loads(request.body).get('searchtxt')
            
        result=WORKER_DETAILS.objects.filter(Worker_id=search_str) 
        data=result.values()
        return JsonResponse(list(data), safe=False)

def add_sugg(request):
    if request.method == 'POST':
        typeofwork=json.loads(request.body).get('type')
        sugg=json.loads(request.body).get('sugg')
        s=suggestions()
        s.Type=typeofwork
        s.suggestion=sugg
        s.save()
   
        result=suggestions.objects.filter(Type=typeofwork) 
        data=result.values()
        return JsonResponse(list(data), safe=False)

def save_project(request):
    p=tbl_projects()
    p.Customer_id=request.POST.get('userid')
    p.p_name=request.POST.get('pname')
    p.Type=request.POST.get('fieldofwork')
    p.D_start=request.POST.get('sdate')
    p.D_end=request.POST.get('edate')
    p.lat=request.POST.get('lat')
    p.lon=request.POST.get('lon')
    p.Loc=request.POST.get('city')
    fs=FileSystemStorage()
    Photo=request.FILES['pimage']
    fn=fs.save(Photo.name,Photo)
    uploaded_file_url=fs.url(fn)
    p.Plan_img=uploaded_file_url
    p.Suggestion=request.POST.get('user_suggestion')
    p.remark=request.POST.get('remarks')
    p.save()
    messages.success(request, 'Project Added Successfully')
    return redirect('/login_cus/')

def view_project(request):
    if 'cusid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        cusid=request.session['cusid']
        d=CUSTOMER_DETAILS.objects.get(cu_name=cusid)
        cid=d.Customer_id
        p=tbl_projects.objects.filter(Customer_id=cid).order_by('id')
        return render(request, 'view_project.html',{'p':p})

def show_contractor(request):
    if request.method == 'POST':
        pid=json.loads(request.body).get('id')
        p=tbl_projects.objects.get(id=pid)
        c=p.Loc
        type=p.Type

        result=CONTRACTOR_DETAILS.objects.filter(Field_of_work=type) & (CONTRACTOR_DETAILS.objects.filter(city=c))
        data=result.values()
        return JsonResponse(list(data), safe=False)

def invite_contractor(request):
    if request.method == 'POST':
        cid=json.loads(request.body).get('id')
        cusid=json.loads(request.body).get('cusid')
        con=CONTRACTOR_DETAILS.objects.get(Contractor_id=cid)
        d=DETAILS.objects.get(D_id=cid)
        email=d.Email
        pid=json.loads(request.body).get('pid')
        data=idgenerator.objects.get(id=1)

        cinvite=tbl_contractor_invite()
        cinvite.Project_id=pid
        cinvite.Contractor_id=cid
        cinvite.status='0'
        con.p_sts_id=cusid
        con.save()
        cinvite.save()
        subject = 'Invitation'
        message = f'You got a Quoatation Invitation.'
        email_from = myapp.settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list )
            
        result=tbl_contractor_invite.objects.filter(Project_id=pid)
        data=result.values()
        return JsonResponse(list(data), safe=False)

def view_invite_con(request,id):
    if 'conid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        p=tbl_contractor_invite.objects.filter(status='0') & tbl_contractor_invite.objects.filter(Contractor_id=id)
        list = []
        for a in p:
            pd=tbl_projects.objects.get(id=a.Project_id)
            list.append(pd)
        return render(request,'view_invite_con.html',{'p':p,'l':list,'id':id})

def add_image_con(request):
    if 'conid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        d=Photos()
        d.userid=request.POST.get('userid')
        d.Title=request.POST.get('title')
        d.user_name=request.POST.get('uname')
        Photo=request.FILES['photo']
        print("ph",Photo)
        fs=FileSystemStorage()
        fn=fs.save(Photo.name,Photo)
        uploaded_file_url=fs.url(fn)
        d.image=uploaded_file_url
        d.save()
        messages.success(request, 'Image added Successfully')
        return redirect('/login_con/')   
def show_image_con(request,Contractor_id):
    if 'conid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        d=Photos.objects.filter(userid=Contractor_id)
        return render(request,"show_image_con.html",{"data":d})

    
def accept_invite_con(request,id,Customer_id,cid):
    p=tbl_contractor_invite.objects.get(Contractor_id=cid, Project_id=id)
    data=CONTRACTOR_DETAILS.objects.get(Contractor_id=cid)
    name=data.c_name
    d=DETAILS.objects.get(D_id=Customer_id)
    email=d.Email
    subject = 'Invitation'
    message = f'{name} Just Accepted Your Invite \n He will Submit the quoatation Shortly'
    email_from = myapp.settings.EMAIL_HOST_USER        
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
    p.status='1'
    p.save()
    return redirect('/login_con/')

def reject_invite_con(request,id,Customer_id,cid):
    p=tbl_contractor_invite.objects.get(Contractor_id=cid, Project_id=id)
    data=CONTRACTOR_DETAILS.objects.get(Contractor_id=cid)
    name=data.c_name
    d=DETAILS.objects.get(D_id=Customer_id)
    email=d.Email
    subject = 'Invitation'
    message = f'{name} Just Rejected Your Invite \n Dont Worry We got You Covered'
    email_from = myapp.settings.EMAIL_HOST_USER        
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
    p.status='2'
    p.save()
    return redirect('/login_con/')

def manage_project(request,pid):
    if 'conid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        conid=request.session['conid']
        c=CONTRACTOR_DETAILS.objects.get(c_name=conid)
        cd=DETAILS.objects.get(D_id=c.Contractor_id)
        t=TYPE_OF_WORK.objects.get(Type_of_work=c.Field_of_work)
        rates=RATES.objects.get(Type_id=t.Type_id)
        pd=tbl_projects.objects.get(id=pid)
        d=DETAILS.objects.get(D_id=pd.Customer_id)
        try:
            r=tbl_payment_request.objects.get(Project_id=pid,Contractor_id=c.Contractor_id,Customer_id=pd.Customer_id,status='0')
            t=tbl_payments.objects.filter(rpayment_id=r.id).last()
            try:
                p=tbl_progress.objects.get(project_id=pid)
                return render(request,'manage_project.html',{'pd':pd,'d':d,'r':rates,'c':cd,'u':c,'pay':r,'t':t,'p':p})
            except tbl_progress.DoesNotExist:
                return render(request,'manage_project.html',{'pd':pd,'d':d,'r':rates,'c':cd,'u':c,'pay':r,'t':t})
        except tbl_payment_request.DoesNotExist:
            return render(request,'manage_project.html',{'pd':pd,'d':d,'r':rates,'c':cd,'u':c})
def cal_estimate(request):
    if request.method == 'POST':
        area=json.loads(request.body).get('a')
        rate=json.loads(request.body).get('r')
        tid=json.loads(request.body).get('t')
        total=int(area)*int(rate)
        tdata=TYPE_OF_WORK.objects.get(Type_id=tid)
        t=tdata.Type_of_work
        if t == 'Construction':
            split_estimate={
                "cement": pcalculate(16.4,total),
                "sand": pcalculate(12.3,total),
                "aggregate":pcalculate(7.4,total),
                "steel":pcalculate(24.6,total),
                "finishers":pcalculate(16.5,total),
                "fittings":pcalculate(22.8,total),
                "total":"{:,}".format(total),
                "total_cost":total,
                "firstm":pcalculate1(21.9,total),
                "secondm":pcalculate1(18.4,total),
                "thirdm":pcalculate1(11.1,total),
                "fourthm":pcalculate1(16.9,total),
                "fifthm":pcalculate1(17.8,total),
                "sixthm":pcalculate1(13.9,total),
            }
        data=split_estimate
        return JsonResponse(data, safe=False)
        
def pcalculate(percentage,value):
    p = round(value * (float(percentage)/100))
    return ("{:,}".format(p))

def pcalculate1(percentage,value):
    p = round(value * (float(percentage)/100))
    return p

def add_quotation(request):
    pid=request.POST.get('pid')
    cid=request.POST.get('cid')
    cusid=request.POST.get('cusid')
    q=tbl_quotation.objects.filter(Project_id=pid,Contractor_id=cid)
    if(q.count()>0):
        q=tbl_quotation.objects.get(Project_id=pid,Contractor_id=cid)
        q.amt=request.POST.get('amount')
        fs=FileSystemStorage()
        file=request.FILES['estimatepdf']
        fn=fs.save(file.name,file)
        uploaded_file_url=fs.url(fn)
        q.file=uploaded_file_url
        q.save()
        d=DETAILS.objects.get(D_id=cusid)
        c=CONTRACTOR_DETAILS.objects.get(Contractor_id=cid)
        name=c.c_name
        Email=d.Email
        subject = 'Quotation'
        message = f'{name} Just Updated His Quotation\nCheck It Out👍'
        email_from = myapp.settings.EMAIL_HOST_USER        
        recipient_list = [Email]
        send_mail( subject, message, email_from, recipient_list )
        messages.success(request, 'Quotation Updated')
        return redirect('manage_project', pid=pid)
    else:
        q=tbl_quotation()
        q.Project_id=request.POST.get('pid')
        q.Contractor_id=request.POST.get('cid')
        q.Customer_id=request.POST.get('cusid')
        d=DETAILS.objects.get(D_id=cusid)
        c=CONTRACTOR_DETAILS.objects.get(Contractor_id=cid)
        name=c.c_name
        Email=d.Email
        q.amt=request.POST.get('amount')
        fs=FileSystemStorage()
        file=request.FILES['estimatepdf']
        fn=fs.save(file.name,file)
        uploaded_file_url=fs.url(fn)
        q.file=uploaded_file_url
        q.status='0'
        q.save()
        subject = 'Quotation'
        message = f'{name} Just Submitted His Quotation\nCheck It Out👍'
        email_from = myapp.settings.EMAIL_HOST_USER        
        recipient_list = [Email]
        send_mail( subject, message, email_from, recipient_list )
        messages.success(request, 'Quotation Submitted')
        return redirect('manage_project', pid=pid)
def confirm_quotation(request,id):
    if 'cusid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        q=tbl_quotation.objects.get(id=id)
        d=DETAILS.objects.get(D_id=q.Contractor_id)
        c=DETAILS.objects.get(D_id=q.Customer_id)
        name=c.Name
        email=d.Email
        subject = 'Congratulations'
        message = f'{name} Just Accepted Your Quotation \n'
        email_from = myapp.settings.EMAIL_HOST_USER        
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list )
        q.status='1'
        q.save()
        return redirect('/login_cus/')

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
def manage_project_cus(request,pid):
    if 'cusid' not in request.session:
        messages.success(request, 'Session Expired')
        return redirect('/login/')
    else:
        cuid=request.session['cusid']
        d=CUSTOMER_DETAILS.objects.get(cu_name=cuid)
        cusid=d.Customer_id
        try:
            q=tbl_quotation.objects.get(Customer_id=cusid, Project_id=pid, status='1')
            p=tbl_projects.objects.get(id=pid)
            d=DETAILS.objects.get(D_id=q.Contractor_id)
            cid=q.Contractor_id
            try:
                r=tbl_payment_request.objects.get(Project_id=pid,Contractor_id=q.Contractor_id,Customer_id=cusid)
                pa=tbl_payments.objects.filter(rpayment_id=r.id).order_by('-id')[:7]
                rid=str(r.id)
                pid=str(pid)
                currency = 'INR'
                if r.ramt==0:
                    amount= 200
                else:
                    amount = r.ramt*100
            
                # Create a Razorpay Order
                razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                                currency=currency,
                                                                payment_capture='0'))
            
                # order id of newly created order.
                razorpay_order_id = razorpay_order['id']
                callback_url = 'paymenthandler/'+cid+'/'+pid+'/'+rid+'/'+cusid
            
                # we need to pass these details to frontend.
                context = {}
                context['razorpay_order_id'] = razorpay_order_id
                context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
                context['razorpay_amount'] = amount
                context['currency'] = currency
                context['callback_url'] = callback_url
                context['pd']=p
                context['d']=d
                context['q']=q
                context['r']=r
                context['pa']=pa
                try:
                    pro=tbl_progress.objects.get(project_id=pid)
                    context['p']=pro
                    return render(request, 'manage_project_cus.html',context=context)
                except tbl_progress.DoesNotExist:
                    return render(request, 'manage_project_cus.html',context=context)
            except tbl_payment_request.DoesNotExist:
                currency = 'INR'
                return render(request, 'manage_project_cus.html',{'pd':p,'d':d,'q':q})
        except tbl_quotation.DoesNotExist:
            q=None
            messages.success(request, 'This Project Did not Confirmed')
            return redirect('/login_cus/')

def show_estimate(request):
    if request.method == 'POST':
        total=json.loads(request.body).get('a')
        total=float(total)
        split_estimate = {
            "cement": pcalculate(16.4, total),
            "sand": pcalculate(12.3, total),
            "aggregate": pcalculate(7.4, total),
            "steel": pcalculate(24.6, total),
            "finishers": pcalculate(16.5, total),
            "fittings": pcalculate(22.8, total),
            "total": "{:,}".format(total),
            "total_cost": total,
            "firstm": pcalculate1(21.9, total),
            "secondm": pcalculate1(18.4, total),
            "thirdm": pcalculate1(11.1, total),
            "fourthm": pcalculate1(16.9, total),
            "fifthm": pcalculate1(17.8, total),
            "sixthm": pcalculate1(13.9, total),}
        data=split_estimate
        return JsonResponse(data, safe=False)

# Razor pay things ---------------------------------------------------------------------------------------       


@csrf_exempt
def paymenthandler(request,cid,pid,rid,cusid):
    print(cid,rid,cusid,pid)
    # only accept POST request.
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id', '')
        razorpay_order_id = request.POST.get('razorpay_order_id', '')
        signature = request.POST.get('razorpay_signature', '')
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }


        q = tbl_quotation.objects.get(
        Project_id=pid, Contractor_id=cid, Customer_id=cusid, status='1')
        total = q.amt
        c = DETAILS.objects.get(D_id=cusid)
        co = DETAILS.objects.get(D_id=cid)
        pro = tbl_projects.objects.get(id=pid)
        r = tbl_payment_request.objects.get(id=rid)
        p = tbl_payments()
        p.rpayment_id = rid
        p.payment_id = payment_id
        p.pamount = r.ramt
        ramt=r.ramt
        t=tbl_payments.objects.filter(rpayment_id=r.id)
        if t.exists():
            a=t.last()
            try:
                tbl=tbl_payments.objects.get(id=a.id)
                bal_amt=tbl.bamount
                p.bamount = bal_amt-ramt
                p.status = '0'
                p.save()
            except tbl_payments.DoesNotExist:
                p.bamount =total-ramt
                p.status = '0'
                p.save()
        else:
            p.bamount =total-ramt
            p.status = '0'
            p.save()

        try:
           
            # get the required parameters from post request.
            
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            
            if result is None:
                amount = r.ramt  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    
                    
                    pd=tbl_payments.objects.last()
                    r.ramt = 0
                    r.save()
                    # if we don't find the required parameters in POST data
                    return render(request, 'payment_bill.html',{'ramt':ramt,'pd':pd,'c':c,'co':co,'pro':pro})
                except:
                    
                    
                    pd=tbl_payments.objects.last()
                    r.ramt = 0
                    r.save()
                    # if we don't find the required parameters in POST data
                    return render(request, 'payment_bill.html',{'ramt':ramt,'pd':pd,'c':c,'co':co,'pro':pro})
                       
            else:
                
                
                pd=tbl_payments.objects.last()
                r.ramt = 0
                r.save()
                # if we don't find the required parameters in POST data
                return render(request, 'payment_bill.html',{'ramt':ramt,'pd':pd,'c':c,'co':co,'pro':pro})
        except:
            
            
            pd=tbl_payments.objects.last()
            r.ramt = 0
            r.save()
            # if we don't find the required parameters in POST data
            return render(request, 'payment_bill.html',{'ramt':ramt,'pd':pd,'c':c,'co':co,'pro':pro})

    else:
       # if other than POST request is made.
        return HttpResponse('fail2')

def check_project(request):
    if request.method == 'POST':
        pid=json.loads(request.body).get('a')
        cid=json.loads(request.body).get('c')
        try:
            q=tbl_quotation.objects.get(Contractor_id=cid,Project_id=pid,status='1')
            data=q.amt
            return JsonResponse(data, safe=False)
        except tbl_quotation.DoesNotExist:
            data='false'
            return JsonResponse(data, safe=False)

def add_prequest(request):
    if request.method == 'POST':
        pid=json.loads(request.body).get('pid')
        cid=json.loads(request.body).get('cid')
        cusid=json.loads(request.body).get('cusid')
        ramt=json.loads(request.body).get('ramt')
        d=DETAILS.objects.get(D_id=cusid)
        cd=DETAILS.objects.get(D_id=cid)
        name=cd.Name
        email=d.Email
        try:
            r=tbl_payment_request.objects.get(Project_id=pid,Contractor_id=cid,Customer_id=cusid,status='0')
            r.ramt=ramt
            r.save()
            subject = 'Payment'
            message = f'{name} Just Requested For {ramt} Rupees \n'
            email_from = myapp.settings.EMAIL_HOST_USER        
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            rd=tbl_payment_request.objects.filter(Project_id=pid,Contractor_id=cid,Customer_id=cusid,status='0')
            data=rd.values()
            return JsonResponse(list(data), safe=False)
        except tbl_payment_request.DoesNotExist:
            r=tbl_payment_request()
            r.Project_id=pid
            r.Contractor_id=cid
            r.Customer_id=cusid
            r.ramt=int(ramt)
            r.status='0'
            r.save()
            subject = 'Payment'
            message = f'{name} Just Requested For {ramt} Rupees \n'
            email_from = myapp.settings.EMAIL_HOST_USER        
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            rd=tbl_payment_request.objects.filter(Project_id=pid,Contractor_id=cid,Customer_id=cusid,status='0')
            data=rd.values()
            return JsonResponse(list(data), safe=False)

def add_progress(request):
    pid=request.POST.get('p_pid')
    progress=request.POST.get('percentage')
    label=request.POST.get('cwork')
    try:
        p=tbl_progress.objects.get(project_id=pid)
        p.label=label
        p.progress=progress
        p.save()
        messages.success(request, 'Progress Upadated')
        return redirect('manage_project', pid=pid)
    except tbl_progress.DoesNotExist:
        p=tbl_progress()
        p.project_id=pid
        p.label=label
        p.progress=progress
        p.save()
        messages.success(request, 'Progress Started')
        return redirect('manage_project', pid=pid)

def add_review_cus(request):
    from1=request.POST.get('from')
    to=request.POST.get('to')
    review=request.POST.get('review')
    pid=request.POST.get('pid')
    rating=request.POST.get('star')
    try:
        p=tbl_rating.objects.get(to_id=to, project_id=pid)
        p.review=review
        p.rating=rating
        p.save()
        if 'CON' in from1:
            messages.success(request, 'Review Updated')
            return redirect('manage_project', pid=pid)
        else:
            messages.success(request, 'Review Updated')
            return redirect('manage_project_cus', pid=pid)
    except tbl_rating.DoesNotExist:
        p=tbl_rating()
        p.review=review
        p.rating=rating
        p.project_id=pid
        p.from_id=from1
        p.to_id=to
        p.save()
        if 'CON' in from1:
            messages.success(request, 'Review Added')
            return redirect('manage_project', pid=pid)
        else:
            messages.success(request, 'Review Added')
            return redirect('manage_project_cus', pid=pid)
def show_review(request):
    if request.method == 'POST':
        pid=json.loads(request.body).get('pid')
        to=json.loads(request.body).get('to')
        from1=json.loads(request.body).get('from')
        t=tbl_rating.objects.filter(from_id=from1,project_id=pid)
        data=t.values()
        return JsonResponse(list(data), safe=False)


