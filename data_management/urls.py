from django.urls import path
from .views import DataManagementMain


urlpatterns = [
    path('',DataManagementMain.as_view(),name="data_management_main_view")
]