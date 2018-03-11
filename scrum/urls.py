from django.conf.urls import url
from scrum import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^backlog/(\d+)/$', views.backlog, name='backlog'),
	url(r'^project/$', views.project, name='project'),
	url(r'^sprint/(\d+)/$', views.sprint, name='sprint'),
	url(r'^register/$',views.register,name='register'),
	url(r'^getstory/$',views.getstory,name='getstory'),
	url(r'^getsprint/$',views.getsprint,name='getsprint'),
	url(r'^getproject/$',views.getproject,name='getproject'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),	
	url(r'^board/(\d+)/$', views.board, name='board'),	
	url(r'^xstory/$', views.xstory, name='xstory'),	
	url(r'^xproject/$', views.xproject, name='xproject'),	
	url(r'^xsprint/$', views.xsprint, name='xsprint'),
	url(r'^geospatial/$',views.geospatial,name='geospatial'),
]