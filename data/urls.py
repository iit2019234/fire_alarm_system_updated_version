from django.urls import path
from . import views
urlpatterns = [
    #path('', views.home),
    path("",views.index,name='home'),
    path("loginpage/",views.loginpage,name='loginpage'),
    path("registerPage/",views.registerPage,name='registerPage'),
    path("dashboard/",views.dashboard,name='dashboard'),
    path("logoutuser/",views.logoutuser,name="logoutuser"),
    path("history/",views.history,name="history"),
    path("graph/",views.graph,name="graph"),
]