from django.urls import path
from posts import views

urlpatterns = [
    path('posts',views.PostList.as_view() ),
    path('posts/<int:pk>/vote',views.VoteCreate.as_view() ),
    
]