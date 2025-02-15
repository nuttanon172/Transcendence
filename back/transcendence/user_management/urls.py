from django.contrib import admin
from django.urls import path, re_path, include
from .views import *

urlpatterns = [
	re_path('login', login.as_view()),
	re_path('signup', signup.as_view()),
	re_path('logout', logout.as_view()),
	re_path('profile', profile.as_view()),
	re_path('update_user', UpdateUser.as_view()),
	re_path('user_avatar', UserAvatar.as_view()),
	re_path('add_friend', AddFriend.as_view()),
	re_path('remove_friend', RemoveFriend.as_view()),
	re_path('friends_list', FriendsList.as_view()),
	re_path('users_list', UsersList.as_view()),
	]
