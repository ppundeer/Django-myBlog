from django.urls import path
from .views import postList, postDetail, postCreate, postUpdate, postDelete
from . import views

urlpatterns = [
    path('', postList.as_view(), name='homepage'),
    path('post/<int:pk>/', postDetail.as_view(), name='postdetail'),
    path('post/new/', postCreate.as_view(), name='postcreate'),
    path('post/<int:pk>/update/', postUpdate.as_view(), name='postupdate'),
    path('post/<int:pk>/delete/', postDelete.as_view(), name='postdelete'),
    path('about/', views.about, name='aboutpage'),
]