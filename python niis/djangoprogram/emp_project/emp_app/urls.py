from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_emp),
    path('view/', views.view_emp),
    path('edit/<int:id>/', views.edit_emp),
    path('update/<int:id>/', views.update_emp),
    path('delete/<int:id>/', views.delete_emp),
]