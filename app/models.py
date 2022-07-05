from email.headerregistry import Address
from django.db import models
from django.db.models.fields.related import ForeignKey
from matplotlib.pyplot import cla

#Create your models here.
class LOGIN(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    type=models.CharField(max_length=10)

    class Meta:
        db_table = "LOGIN"
class DETAILS(models.Model):
    D_id=models.CharField(max_length=10)
    Name=models.CharField(max_length=20)
    Address=models.CharField(max_length=200)
    Ph_no=models.CharField(max_length=10)
    Email=models.CharField(max_length=50)
    Rating=models.CharField(max_length=5)

    class Meta:
        db_table = "DETAILS"
class CUSTOMER_DETAILS(models.Model):
    Customer_id=models.CharField(max_length=10)
    D_id=models.CharField(max_length=10)
    cu_name=models.CharField(max_length=20)
    status=models.CharField(max_length=30)
    password=models.CharField(max_length=15)


    class Meta:
        db_table = "CUSTOMER_DETAILS"
class CONTRACTOR_DETAILS(models.Model):
    Contractor_id=models.CharField(max_length=10)
    c_name=models.CharField(max_length=20)
    Field_of_work=models.CharField(max_length=50)
    exp=models.CharField(max_length=20)
    months=models.CharField(max_length=10)
    city=models.CharField(max_length=30)
    pincode=models.CharField(max_length=10)
    lic_no=models.CharField(max_length=20)
    status=models.CharField(max_length=30)
    password=models.CharField(max_length=15)
    profile_image=models.CharField(max_length=100)
    p_sts_id=models.CharField(max_length=10)



    class Meta:
        db_table = "CONTRACTOR_DETAILS"
class WORKER_DETAILS(models.Model):
    Worker_id=models.CharField(max_length=10)
    Fd_of_work=models.CharField(max_length=50)
    exp=models.CharField(max_length=20)
    months=models.CharField(max_length=10)
    city=models.CharField(max_length=30)
    pincode=models.CharField(max_length=10)
    U_name=models.CharField(max_length=20)
    status=models.CharField(max_length=30)
    password=models.CharField(max_length=15)
    profile=models.CharField(max_length=30)
    profile_image=models.CharField(max_length=100)


    class Meta:
        db_table = "WORKER_DETAILS"
class COMPANY_DETAILS(models.Model):
    Company_id=models.CharField(max_length=10)
    co_name=models.CharField(max_length=20)
    li_no=models.CharField(max_length=20)
    status=models.CharField(max_length=30)
    password=models.CharField(max_length=15)


    class Meta:
        db_table = "COMPANY_DETAILS"
class TYPE_OF_WORK(models.Model):
    Type_id=models.CharField(max_length=10)
    Type_of_work=models.CharField(max_length=30)

    class Meta:
        db_table="TYPE_OF_WORK"
class RATES(models.Model):
    Rate_id=models.CharField(max_length=10)
    Type_id=models.CharField(max_length=20)
    Rate=models.IntegerField()
    Rate_type=models.CharField(max_length=20)



    class Meta:
        db_table = "RATES"
class SHOP_DETAILS(models.Model):
    Shop_id=models.CharField(max_length=10)
    Shop_name=models.CharField(max_length=20)
    Address=models.CharField(max_length=200)
    City=models.CharField(max_length=30)
    pincode=models.CharField(max_length=10)
    Ph_no=models.CharField(max_length=10)
    Type_id=models.CharField(max_length=10)


    class Meta:
        db_table = "SHOP_DETAILS"
class idgenerator(models.Model):
    cuid=models.IntegerField()
    coid=models.IntegerField()
    wid=models.IntegerField()
    cid=models.IntegerField()
    rid=models.IntegerField()
    tid=models.IntegerField()
    sid=models.IntegerField()
    did=models.IntegerField()
    pid=models.IntegerField()
    

    class Meta:
        db_table = "idgenerator"
class Photos(models.Model):
    userid=models.CharField(max_length=20)
    user_name=models.CharField(max_length=20)
    Title=models.CharField(max_length=20)
    image=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)

    class Meta:
        db_table = "PHOTOS"

class Messages(models.Model):
    Name=models.CharField(max_length=20)
    Subject=models.CharField(max_length=100)
    Message=models.CharField(max_length=200)
    Email=models.CharField(max_length=20)
    date=models.DateField(auto_now_add=True)

    class Meta:
        db_table = "MESSAGES"

class profiles(models.Model):
    userid=models.CharField(max_length=10)
    type=models.CharField(max_length=30)
    link=models.CharField(max_length=100)

    class Meta:
        db_table = "PROFILES"

class work_invite(models.Model):
    Type=models.CharField(max_length=30)
    Desc=models.CharField(max_length=100)
    Loc=models.CharField(max_length=30)
    Worker_id=models.CharField(max_length=20)
    Customer_id=models.CharField(max_length=20)
    Status=models.CharField(max_length=5)

    class Meta:
        db_table = "WORK_INVITE"



class suggestions(models.Model):
    Type=models.CharField(max_length=30)
    suggestion=models.CharField(max_length=200)

    class Meta:
        db_table ="suggestions"

class materials(models.Model):
    M_name=models.CharField(max_length=50)
    Type=models.CharField(max_length=30)

    class Meta:
        db_table ="materials"

class tbl_projects(models.Model):
    Customer_id=models.CharField(max_length=20)
    p_name=models.CharField(max_length=50)
    Type=models.CharField(max_length=50)
    D_start=models.DateField()
    D_end=models.DateField()
    lat=models.FloatField(max_length=50)
    lon=models.FloatField(max_length=50)
    Loc=models.CharField(max_length=30)
    Plan_img=models.CharField(max_length=100)
    Suggestion=models.CharField(max_length=100)
    remark=models.CharField(max_length=200)

    class Meta:
        db_table ="tbl_projects"

class tbl_contractor_invite(models.Model):
    Project_id=models.CharField(max_length=5)
    Contractor_id=models.CharField(max_length=10)
    status=models.CharField(max_length=5)

    class Meta:
        db_table ="tbl_contractor_invite"

class tbl_quotation(models.Model):
    Project_id=models.CharField(max_length=5)
    Contractor_id=models.CharField(max_length=10)
    Customer_id=models.CharField(max_length=10)
    amt=models.IntegerField()
    file=models.CharField(max_length=100)
    status=models.CharField(max_length=5)

    class Meta:
        db_table ="tbl_quotation"

class tbl_payment_request(models.Model):
    Project_id=models.CharField(max_length=5)
    Contractor_id=models.CharField(max_length=10)
    Customer_id=models.CharField(max_length=10)
    ramt=models.IntegerField()
    status=models.CharField(max_length=5)

    class Meta:
        db_table ="tbl_payment_request"

class tbl_payments(models.Model):
    rpayment_id=models.CharField(max_length=10)
    payment_id=models.CharField(max_length=10)
    pamount=models.IntegerField()
    bamount=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=5)

    class Meta:
        db_table ="tbl_payments"