
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from scrum import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^scrum/', include('scrum.urls')),	
	url(r'^admin/', admin.site.urls),
]
