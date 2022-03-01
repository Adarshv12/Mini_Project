"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('signup/',views.signup),
    path('register/',views.register),
    path('login/',views.login),
    path('application/',views.application),
    path('signup_customer/',views.signup_customer),
    path('signup_contractor/',views.signup_contractor),
    path('signup_company/',views.signup_company),
    path('signup_worker/',views.signup_worker),
    path('customer_registration/',views.customer_registration),
    path('worker_registration/',views.worker_registration),
    path('contractor_registration/',views.contractor_registration),
    path('company_registration/',views.company_registration),
    path('login_user/',views.login_user),
    path('edit_cus/<Customer_id>',views.edit_cus),
    path('edit_con/<Contractor_id>',views.edit_con),
    path('edit_wor/<Worker_id>',views.edit_wor),
    path('edit_com/<Company_id>',views.edit_com),
    path('approve_cus/',views.approve_cus),
    path('reject_cus/<D_id>',views.reject_cus),
    path('approve_con/<D_id>',views.approve_con),
    path('reject_con/<D_id>',views.reject_con),
    path('approve_wor/<D_id>',views.approve_wor),
    path('reject_wor/<D_id>',views.reject_wor),
    path('approve_com/',views.approve_com),
    path('reject_com/<D_id>',views.reject_com),
    path('logout/',views.logout),
    path('add_rates/',views.add_rates),
    path('admin_header/',views.admin),
    path('add_shop/',views.add_shop),
    path('show_shops/',views.show_shops),
    path('show_rates/',views.show_rates),
    path('login_admin/',views.login_admin),
    path('logout_worker/',views.logout_worker),
    path('login_worker/',views.login_worker),
    path('test/',views.test),
    path('add_image/',views.add_image),
    path('show_image/<Worker_id>',views.show_image),
    path('message/',views.message),
    path('login_cus/',views.login_cus),
    path('edit_rate/',views.edit_rate),
    path('del_rate/<Rate_id>',views.del_rate),
    path('del_shop/<Shop_id>',views.del_shop),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
