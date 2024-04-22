from django.urls import path
from .views import SchooolsMain,ClassesMain,SubjectsMain


urlpatterns = [
    path('schools',SchooolsMain.as_view(),name="schools_main_view"),
    path('classess',ClassesMain.as_view(),name="classes_main_view"),
    path('subjects',SubjectsMain.as_view(),name="subjects_main_view"),
]