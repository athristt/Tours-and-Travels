# Here we must define paths to different web pages

from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name = "index"), # this code serves the http response from the views.py
    path("about", views.about, name = "about"),
    path("packages/", views.package, name = "package"),
    path("guide/", views.guide, name = "guide"),
    path("blog/", views.blog, name = "blog"),
    path('blog/<slug:slug>/', views.post_detail, name= "post_detail"),# using slug insted of id to path
    path('packages/<slug:slug>/', views.package_details, name='package_detail'), # defining URL path for slug Capture
    path("FAQ", views.FAQ, name = "FAQ"),
    path("TermsandCondition", views.TermsandCondition, name = "TermsandCondition"),
    path("form", views.form, name = "form"),
    path("registered/", views.thankyou, name='thankyou'),
    path("review", views.review, name = "review"),
    path("reviewed/", views.success, name='success'), 
]