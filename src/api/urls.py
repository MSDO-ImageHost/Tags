from django.urls import path
from .views import TagView

urlpatterns = [
    path('home', TagView.as_view())
]
