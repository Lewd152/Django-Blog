from django.conf.urls import url
from Blog import views

urlpatterns = [
    url(r'^/', views.selectAll),
    url(r'^selectgroup/', views.selectGroup),
    url(r'^selectKeyword/', views.selectKeyword),

]