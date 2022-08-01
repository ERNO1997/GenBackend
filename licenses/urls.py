from licenses import views
from django.urls import path


urlpatterns = [
    path('status', views.LicenseStatusAPIView.as_view(), name='license_status'),
    path('list', views.LicenseListAPIView.as_view(), name='license_list'),
]
