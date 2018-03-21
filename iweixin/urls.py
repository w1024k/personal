# coding:utf-8
from app import profile

urlpatterns = [
    (r"/", profile.Test),
    (r"/login/", profile.Login),
    (r"/get/friends/", profile.GetFriends),
]
