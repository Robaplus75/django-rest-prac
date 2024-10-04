from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductMixinView.as_view()),
    path('create/', views.ProductCreateAPIView.as_view()),
]