from django.urls import path
from . import views

urlpatterns = [
    path('voter-check/<int:birth_year>/', views.voter_status, name='voter_check'),
    path('check-password/', views.password_checker_view, name='password_checker'),

]



