
from django.urls import path,include
from moneyapp import views

urlpatterns = [
   path('',views.index),
   path('account',views.account),
   path('forninput/',views.input,name='forninput'),
   path('delete/<statement_id>',views.delete,name='delete'),
]