from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    #login
    path("login/",views.login,name="login"),
    path("logindata/",views.logindata,name="logindata"),


    #signup
    path('signup/',views.signup,name="signup"),


    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("addfriend/<str:name>", views.addFriend, name="addFriend"),
    path("chat/<str:username>", views.chat, name="chat"),
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('api/messages', views.message_list, name='message-list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
