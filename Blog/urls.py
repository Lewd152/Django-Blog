from django.conf.urls import url
from Blog import views

urlpatterns = [
    url(r'^/', views.selectAll),
    url(r'^selectgroup/', views.selectGroup),
    url(r'^selectKeyword/', views.selectKeyword),
    url(r'^insertarticle/', views.installArticle),
    url(r'^deletearticle/', views.deleteArticle),
    url(r'^index/', views.index),
    url(r'^delete/', views.delete),

]