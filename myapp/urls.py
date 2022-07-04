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
from django.conf.urls import include,url


urlpatterns = [
    path('',views.index),
    path('admin/', admin.site.urls),
    url('', include('app.urls')),

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
    path('edit_con/<Contractor_id>,<status>',views.edit_con),
    path('edit_wor/<Worker_id>,<status>',views.edit_wor),
    path('edit_com/<Company_id>',views.edit_com),
    path('approve_cus/',views.approve_cus),
    path('approve1_cus/<D_id>',views.approve1_cus),

    path('reject_cus/<D_id>',views.reject_cus),
    path('approve_con/<D_id>',views.approve_con),

    path('approve1_con/<D_id>',views.approve1_con),

    path('reject_con/<D_id>',views.reject_con),
    path('reject1_con/<D_id>',views.reject1_con),
    path('approve_wor/<D_id>',views.approve_wor),
    path('approve1_wor/<D_id>',views.approve1_wor),

    path('reject_wor/<D_id>',views.reject_wor),
    path('reject1_wor/<D_id>',views.reject1_wor),
    path('approve_com/',views.approve_com),
    path('approve1_com/<D_id>',views.approve1_com),

    path('reject_com/<D_id>',views.reject_com),
    path('logout/',views.logout),
    path('add_rates/',views.add_rates),
    path('admin_header/',views.admin),
    path('add_shop/',views.add_shop),
    path('show_shops/',views.show_shops),
    path('show_rates/',views.show_rates),
    path('login_admin/',views.login_admin),
    path('logout_worker/',views.logout_worker),
    path('logout_con/',views.logout_con),

    path('login_worker/',views.login_worker),
    path('login_con/',views.login_con),


    path('test/',views.test),
    path('add_image/',views.add_image),
    path('show_image/<Worker_id>',views.show_image),
    path('message/',views.message),
    path('login_cus/',views.login_cus),
    path('logout_cus/',views.logout_cus),
    path('edit_rate/',views.edit_rate),
    path('del_rate/<Rate_id>',views.del_rate),
    path('del_shop/<Shop_id>',views.del_shop),
    path('view_search/<D_id>',views.view_search),
    path('worker_edit/<Worker_id>',views.worker_edit),
    path('update_worker/',views.update_worker),
    path('user_edit/<Customer_id>',views.user_edit),
    path('update_user/',views.update_user),

    path('add_work_invite/',views.add_work_invite),
    path('winvite_accept/<id>',views.winvite_accept),
    path('winvite_reject/<id>',views.winvite_reject),
    path('winvite_view/<id>',views.winvite_view),
    path('worker_back/',views.worker_back),
    path('view_winvite/<uname>',views.view_winvite),
    

    path('add_project/',views.add_project),
    path('save_project/',views.save_project),
    path('view_project/',views.view_project),


    path('contractor_edit/<Contractor_id>',views.contractor_edit),
    path('update_contractor/',views.update_contractor),
    path('view_invite_con/<id>',views.view_invite_con),
    path('manage_project/<pid>',views.manage_project,name='manage_project'),
    path('add_image_con/',views.add_image_con),
    path('show_image_con/<Contractor_id>',views.show_image_con),
    path('accept_invite_con/<int:id>/<str:Customer_id>/<str:cid>',views.accept_invite_con),
    path('add_quotation/',views.add_quotation),
    path('reject_invite_con/<int:id>/<str:Customer_id>/<str:cid>',views.reject_invite_con),
    path('manage_project_cus/<pid>',views.manage_project_cus,name='manage_project_cus'),
    path('confirm_quotation/<int:id>',views.confirm_quotation),

    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
