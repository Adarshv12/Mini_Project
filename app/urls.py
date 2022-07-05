from django.conf.urls import url
from . import views
from .views import dataview
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

app_name = "app"

urlpatterns = [
        path('index/data',dataview.as_view(),name='dataview'),
        url(r'^$', views.index, name='index'),  # index view at /
        url(r'^profile/$', views.profile, name='profile'),
        path('search-users', csrf_exempt(views.user_search),name='search-users'),
        path('search-type', csrf_exempt(views.type_search),name='search-type'),
        path('search-place', csrf_exempt(views.place_search),name='search-place'),
        path('search-pin', csrf_exempt(views.pin_search),name='search-pin'),   # likepost view at /likepost
        path('view_user', csrf_exempt(views.view_user),name='view_user'),   # likepost view at /likepost
        path('type-select', csrf_exempt(views.type_select),name='type-select'),
        path('get-worker_id', csrf_exempt(views.get_worker_id),name='get-worker_id'),   # likepost view at /likepost
        path('add-sugg', csrf_exempt(views.add_sugg),name='add-sugg'),
        path('show-contractor', csrf_exempt(views.show_contractor),name='show-contractor'),
        path('invite-contractor', csrf_exempt(views.invite_contractor),name='invite-contractor'),   # likepost view at /likepost
        path('cal-estimate', csrf_exempt(views.cal_estimate),name='cal-estimate'),   # likepost view at /likepost
        path('show-estimate', csrf_exempt(views.show_estimate),name='show-estimate'),   # likepost view at /likepost
        path('check-project', csrf_exempt(views.check_project),name='check-project'),   # likepost view at /likepost
        path('add-prequest', csrf_exempt(views.add_prequest),name='add-prequest'),   # likepost view at /likepost

        

           
   ]
