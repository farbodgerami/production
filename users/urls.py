from django.urls import path
from . import views

urlpatterns = [
    path("UserlistByAdmin/", views.UserlistByAdmin.as_view(), name="users"),
    path("UserdetailByadmin/<int:id>/", views.UserdetailByadmin.as_view(), name="usersprofile"),
    path("UserregisterByuser/", views.UserregisterByuser.as_view(), name="updateusersprofile"),
    path("UserdetailByuser/", views.UserdetailByuser.as_view(), name="user"),
    path("login/", views.loginman, name="token_obtain_pair"),
    path("logoutview/", views.logoutview,name='logout'  ),
    path('request/<str:sendedplan>/<int:price>/', views.send_request, name='request'),
    path('verify/', views.verify , name='verify'),
]