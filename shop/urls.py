from django.urls import path
from . import views

urlpatterns=[
    path('',views.hm,name='chm'),
    path('<slug:c_slug>/',views.hm,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.prodDetails,name='details'),
    path('search',views.searching,name='search'),

]