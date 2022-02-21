from email.headerregistry import Address
from django.db import models
from django.db.models.fields.related import ForeignKey

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
    W_img=models.CharField(max_length=100)
    status=models.CharField(max_length=30)
    password=models.CharField(max_length=15)


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
    img=models.CharField(max_length=100)
    status=models.CharField(max_length=30)
    password=models.CharField(max_length=15)


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
    M_name=models.CharField(max_length=10)
    M_Rate=models.IntegerField()


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

    class Meta:
        db_table = "idgenerator"
