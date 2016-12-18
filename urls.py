from django.conf.urls import include, url
from django.contrib import admin




admin.site.site_header = 'Suyati Uptime'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('addServer.urls')),
    

]
 