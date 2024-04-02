# PostByUser/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create_board/', views.create_board, name='create_board'),
    path('board_list/', views.board_list, name='board_list'),
    path('create_pin/', views.create_pin,
         name="create_pin"),  # Ensure name is set
    path('list_pins', views.list_pins, name='list_pins'), path(
        'update_pin/<int:pin_id>/', views.update_pin, name='update_pin'),
    path('delete_pin/<int:pin_id>/', views.delete_pin, name='delete_pin'),
    path('', views.home, name='home_page'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('post/<int:image_post_id>/add_comment/',
         views.add_comment, name='add_comment'),
    path('post/<int:image_post_id>/list_comments/',
         views.list_comments, name='list_comments'),

    # this is for the rest of the profile ones
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profile/follow/<int:user_id>/',
         views.adding_followers, name='adding_followers'),
    path('profile/unfollow/<int:following_id>/',



         views.unfollowing, name='unfollowing'),
    path('profile/removefollower/<int:follower_id>/',
         views.removing_follower, name='removing_follower'),
]
