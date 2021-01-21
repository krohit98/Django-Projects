from django.urls import path
from . import views

urlpatterns=[
    path('profile',views.profile,name='profile'),
    path('logout',views.logout,name='logout'),
    path('createPost',views.createPost,name='createPost'),
    path('postComment',views.postComment,name='postComment'),
    path('deletePost',views.deletePost,name='deletePost'),
    path('deleteComment/<str:commentId>',views.deleteComment,name='deleteComment'),
]