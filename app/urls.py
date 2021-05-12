from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from app import views
urlpatterns = [
    path('',views.index,name="home"),
    path('pdf/',views.convertpdf,name="pdf"),
    path('pdf/<int:id>/',views.convertpdf,name="pdffunc"),
    path('download/<int:id>/', views.downloadfile,name="downloadpdf"),
    path('show/',views.showpdf,name="showpdf")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)