from django.contrib import admin
from django.urls import path
import portfolio.views

urlpatterns = [
    path('home/', portfolio.views.home, name='home'),
    path('person/<int:person_id>/',portfolio.views.detail, name='detail'),
    path('person/next/', portfolio.views.person_next, name='next'),
    path('person/<int:person_id>/edit', portfolio.views.person_edit, name='edit'),
    path('person/<int:person_id>/delete', portfolio.views.person_delete, name='delete'),
]