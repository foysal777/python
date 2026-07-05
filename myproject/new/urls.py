from django.urls import path
from . import views

urlpatterns = [
    # <int:birth_year> দিয়ে আমরা বলে দিচ্ছি ইউআরএল থেকে একটা ইন্টিজার ভিউতে পাস হবে
    path('voter-check/<int:birth_year>/', views.voter_status, name='voter_check'),
]