from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^$',views.main_view,name='main_view'),
    url(r'^elec/$', views.elec_view, name='elec'),
    url(r'^start_up/$', views.startup_view, name='startup'),
    url(r'^project/$', views.project_view, name='project'),
    url(r'^experience/$', views.experience_view, name='experience'),
    url(r'^resume/$',views.resume_view, name='resume'),
    url(r'^profile/$',views.profile_view, name='profile'),
    url(r'^post/new/$',views.post_new,name='post_new'),
  #  url(r'^post/detail/$',views.post_detail,name='post_detail'),
]


