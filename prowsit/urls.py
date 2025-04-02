from django.urls import path
from prowsit.views import index

urlpatterns = [
    path('', index)
]

